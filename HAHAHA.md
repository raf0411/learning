• Yes. Your codebase already has the layouts for all three mission types. The next step is connecting mission data → navigation → answer checking → progress.

  I haven’t changed any files. Here’s a walkthrough you can implement yourself, using your existing code.

  ## 1. Understand the pieces you already have

   File                                              Its job
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   CH6-ADA/Models/Mission.swift                      Describes a mission: question, type, choices, command pieces, reward, prerequisites.
  ────────────────────────────────────────────────  ──────────────────────────────────────────────────────────────────────────────────────
   CH6-ADA/Models/MissionCatalog.swift               Holds the missions available in the app. Currently empty.
  ────────────────────────────────────────────────  ──────────────────────────────────────────────────────────────────────────────────────
   CH6-ADA/ViewModels/MissionViewModel.swift         Holds the player’s current answer and will check whether it is correct.
  ────────────────────────────────────────────────  ──────────────────────────────────────────────────────────────────────────────────────
   CH6-ADA/Views/Mission/MissionView.swift           Currently displays the mission selection grid.
  ────────────────────────────────────────────────  ──────────────────────────────────────────────────────────────────────────────────────
   CH6-ADA/ViewModels/MissionBoardViewModel.swift    Groups missions by skill and will update their locked/completed status.
  ────────────────────────────────────────────────  ──────────────────────────────────────────────────────────────────────────────────────
   CH6-ADA/ViewModels/ProfileViewModel.swift         Will record completions, award XP, and calculate progress.

  The distinction to keep in mind:

  - Model: “This question’s correct choice is ls.”
  - ViewModel: “The player selected cd, so this attempt failed.”
  - View: Displays the choices, selection, and feedback.

  Your README is partly outdated: the current MissionView doesn’t switch between playable mission types, and command-piece dragging is already implemented.

  ## 2. Give your missions answers

  Your Mission model currently describes what to display, but doesn’t store what counts as correct.

  Add an answer type in Mission.swift:

  enum MissionAnswer {
      case choice(correctID: String)
      case missingCommand(acceptedValues: [String])
      case arrangement(correctPieceIDs: [String])
  }

  An enum lets each kind of answer carry the data it needs.

  Then extend Mission in three places:

  1. Add the property: let answer: MissionAnswer?
  2. Add an initializer parameter: answer: MissionAnswer? = nil
  3. Assign it inside the initializer: self.answer = answer

  The default nil keeps existing previews working while you add answers. Your validation should report missing answer configuration instead of treating it as success.

  ### Use your existing previews as the first three missions

  You already authored example content in these previews:

   Existing example                Where to find it                                             Answer to add
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Which command lists files?      CH6-ADA/Views/Mission/MultipleChoiceMissionView.swift:47     .choice(correctID: "ls")
  ──────────────────────────────  ───────────────────────────────────────────────────────────  ─────────────────────────────────────────────────────────────────────
   Fill in chmod ___ script.sh     CH6-ADA/Views/Mission/TerminalMissionView.swift:29           .missingCommand(acceptedValues: ["a+x"])
  ──────────────────────────────  ───────────────────────────────────────────────────────────  ─────────────────────────────────────────────────────────────────────
   Arrange cp notes.txt backup/    CH6-ADA/Views/Mission/ArrangeCommandMissionView.swift:302    .arrangement(correctPieceIDs: ["command", "source", "destination"])

  Copy those Mission(...) constructions into MissionCatalog.missions, then:

  - Give them stable IDs, such as "filesystem-list-files".
  - Give the two filesystem missions different order values.
  - Keep them .unlocked while developing.
  - Add their answers.

  Preview data only appears in previews. Putting the missions in the catalog makes them available to the running app.

  For the arrangement mission, keep commandPieces in the scrambled display order. The answer separately stores the correct order.

  ## 3. Connect the screens

  The intended flow can be:

  Home → choose skill → choose mission → play mission

  There are three connections to make.

  ### A. Skill buttons → mission selection

  In CH6-ADA/Views/Home/MissionBoardView.swift:18, you currently create SkillButton() without passing the loop’s skill. That produces five buttons using the default “Filesystem” label.

  For each skill:

  - Display skill.rawValue.capitalized.
  - Navigate to MissionView(missions: viewModel.missions, skill: skill).

  Use NavigationLink for navigation. Refactor SkillButton so its styled label can be used by the link; avoid placing its existing Button inside another interactive control.

  ### B. Mission cards → a playable screen

  CH6-ADA/Views/Home/MissionCardView.swift:16 currently has an empty button action.

  Keep the current MissionView as your picker, and introduce a small MissionPlayView that displays the selected mission:

  import SwiftUI

  struct MissionPlayView: View {
      let mission: Mission

      @StateObject private var viewModel: MissionViewModel

      init(mission: Mission) {
          self.mission = mission
          _viewModel = StateObject(
              wrappedValue: MissionViewModel(mission: mission)
          )
      }

      var body: some View {
          VStack {
              switch mission.type {
              case .terminal:
                  TerminalMissionView(viewModel: viewModel)

              case .multipleChoice:
                  MultipleChoiceMissionView(viewModel: viewModel)

              case .arrangeCommand:
                  ArrangeCommandMissionView(viewModel: viewModel)
              }

              if let feedback = viewModel.feedback {
                  Text(feedback)
              }
          }
          .navigationTitle(mission.title)
      }
  }

  Then make each grid item navigate to MissionPlayView(mission: mission). Refactor the card’s appearance into the link’s label, and disable the link when mission.status == .locked.

  Here, @StateObject gives the playable screen ownership of one attempt. Your three interaction views already use @ObservedObject, so they observe that same attempt.

  ### C. Check this before writing validation

  At this point you should be able to:

  1. Select Filesystem.
  2. See its two missions.
  3. Open either mission and see the matching interaction layout.
  4. Select Permissions and open the missing-command mission.

  ## 4. Implement answer checking for each type

  Keep checking logic in MissionViewModel.

  Your existing methods provide the entry points:

   Type               Player’s answer        Submission method
  ━━━━━━━━━━━━━━━━━  ━━━━━━━━━━━━━━━━━━━━━  ━━━━━━━━━━━━━━━━━━━━━
   Multiple choice    selectedChoiceID       submitChoice()
  ─────────────────  ─────────────────────  ─────────────────────
   Missing command    missingCommandInput    submitCommand(_:)
  ─────────────────  ─────────────────────  ─────────────────────
   Arrange command    arrangedPieces         submitArrangement()

  Have these submission methods prepare the answer and call validateSubmission().

  Inside validation, follow this sequence:

  Confirm a mission and compatible answer rule exist
  → Check whether the player supplied a complete answer
  → Compare it with the rule
  → Set submissionState and feedback
  → Call completeMission() on success

  ### Multiple choice

  Currently, your choices are Text views, so tapping them never calls the existing selectChoice(_:).

  Make each choice a button:

  Button(choice.text) {
      viewModel.selectChoice(choice)
  }

  Keep your existing styling, and change the selected choice’s appearance using:

  viewModel.selectedChoiceID == choice.id

  Add submission:

  Button("Check answer") {
      viewModel.submitChoice()
  }
  .disabled(viewModel.selectedChoiceID == nil)

  Validation compares the selected ID with the answer’s correctID.

  Using IDs means you can change a choice’s displayed text without changing how it is identified.

  ### Missing command

  Your .terminal mission currently uses a fill-in-the-blank layout. Its answer field is missingCommandInput.

  Add:

  Button("Check answer") {
      viewModel.submitCommand(viewModel.missingCommandInput)
  }

  For this mission type, let submitCommand(_:) store the supplied value in missingCommandInput, then validate it.

  Trim whitespace at the beginning and end, then check whether the result appears in acceptedValues.

  For your example:

  Prefix:       chmod
  Player input: a+x
  Suffix:       script.sh

  The answer rule checks the missing fragment, "a+x".

  Keep accepted alternatives explicit. Avoid automatically lowercasing answers because command arguments can be case-sensitive.

  Also, viewModel.input belongs to the separate floating input bar. Reading that field would check the wrong input for this puzzle.

  ### Arrange command

  Your ViewModel already handles placing, moving, and removing pieces. Build on that.

  Add:

  Button("Check answer") {
      viewModel.submitArrangement()
  }

  Validation should:

  1. Require every command slot to be filled.
  2. Read arrangedPieces.map(\.id).
  3. Compare the result with correctPieceIDs.

  For the existing example:

  ["command", "source", "destination"]

  represents:

  cp notes.txt backup/

  Your existing synchronizeArrangedPieces() reads slots in order. Checking that all slots are filled matters because it removes empty slots when building arrangedPieces.

  ### Feedback applies to all three

  Use:

  - .idle before checking.
  - .failure for an incorrect answer.
  - .success for a correct answer.

  Set a helpful feedback message alongside the state. Reset stale feedback when the player changes their answer.

  Your FloatingCommandInput currently has no submission callback. If you later want Enter to perform an action, CH6-ADA/Views/Terminal/TerminalConsoleView.swift:35 already demonstrates the .onSubmit pattern.

  ## 5. Connect completion to XP and unlocking

  A correct attempt and a completed mission are different pieces of state.

  submissionState describes the current attempt. MissionStatus and UserProgress describe the player’s progression.

  The app currently creates separate mission arrays for the board and terminal. Because Mission is a struct, changing one copy won’t update the others.

  Use the completion callback suggested in your existing TODO:

  onComplete: (Mission) -> Void

  Pass it from the app through the mission screens into MissionViewModel. completeMission() calls it after successful validation.

  At the app level, coordinate:

  Profile records completion and awards XP
  → Board recalculates completed/unlocked/locked statuses
  → Terminal receives the updated board missions

  ### In ProfileViewModel

  Implement recordMissionCompletion(_:) so it:

  1. Returns immediately if the mission ID is already completed.
  2. Inserts the ID into completedMissionIDs.
  3. Awards mission.xpReward.
  4. Updates the level.
  5. Recalculates overall and per-skill progress.

  Put the duplicate check before awarding XP, so reopening a mission doesn’t award the same reward again.

  For per-skill totals, this ViewModel needs access to the mission catalog; totalMissionCount alone cannot tell it how many missions belong to Filesystem.

  Progress is:

  completed missions / total missions

  Use floating-point division and return zero when the total is zero.

  ### In MissionBoardViewModel

  Implement updateUnlocks(using:) with these rules:

  ID already completed?
      → completed

  Otherwise, every prerequisite ID completed?
      → unlocked

  Otherwise
      → locked

  With this rule, missions with no prerequisites start unlocked.

  Also make the picker read the observed board’s current missions. Its current stored let missions array is a snapshot and won’t automatically receive later status updates.

  ### Connect the visible progress

  The Home screen’s coins and battery, and the Profile screen’s percentage and coins, currently use hardcoded values.

  Bind the progress displays to calculated progress. Coins need their own reward data if you want them separate from XP; your models currently define XP rewards only.

  ## 6. Add terminal navigation after the missions work

  CH6-ADA/ViewModels/TerminalViewModel.swift handles simulated navigation. You can implement it independently once the three mission types are playable:

  - pwd: append currentPath to history.
  - ls: list skills, or missions within the selected skill.
  - cd: select a skill or accessible mission.
  - cd ..: return to the parent location.
  - help: display relevant commands and hints.

  When currentMission becomes non-nil, TerminalView already presents a sheet. Change its destination to your new MissionPlayView, and pass the same completion callback used by the board.

  Handle sheet dismissal by restoring the appropriate parent path.

  ## Suggested implementation order

  1. Add the three catalog missions and their answers.
  2. Connect skill selection, mission selection, and MissionPlayView.
  3. Make multiple choice work through correct/incorrect feedback.
  4. Implement missing-command checking.
  5. Implement arrangement checking.
  6. Connect completion, XP, unlocks, and visible progress.
  7. Add terminal navigation and then persistence.

  For each mission, verify an empty answer, a wrong answer, and a correct answer. Once rewards work, reopen a completed mission and confirm XP stays unchanged.

  Start with multiple choice: it gives you the shortest complete path through the model, ViewModel, and view. The other two types then reuse the same validation and completion flow.