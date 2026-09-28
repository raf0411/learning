# SwiftUI text-input and binding probe

This probe tests the connection between view-owned state and a control that must
both read and write that state. Use Xcode completion and compiler messages, but do
not look up a completed implementation.

## 1. Complete before running

Consider this incomplete view:

```swift
struct NameEntryView: View {
    @State private var name = ""

    var body: some View {
        VStack {
            TextField("Your name", text: /* TODO */)
            Text("Hello, \(name)")
        }
        .padding()
    }
}
```

What expression should replace `/* TODO */`?

```swift
$name
```

Why does `TextField` need that expression rather than only the current `String`
value?

> because TextField needs to be passed a binded value

## 2. Predictions

Record the complete visible greeting text before running.

| Action                                             | Predicted greeting |
| -------------------------------------------------- | ------------------ |
| Fresh launch                                       | Hello,             |
| Type `Raffi`                                       | Hello, Raffi       |
| Delete all typed characters                        | Hello,             |
| Type `Dina`, fully terminate the app, and relaunch | Hello,             |

## 3. Implement and run

Complete the view in Xcode and make it the displayed content. Paste the code that
actually ran:

```swift
struct NameEntryView: View {
    @State private var name = ""

    var body: some View {
        VStack {
            TextField("Your name", text: $name)
            Text("Hello, \(name)")
        }
        .padding()
    }
}
```

## 4. Actual observations

| Action                                             | Actual greeting | Prediction matched? |
| -------------------------------------------------- | --------------- | ------------------- |
| Fresh launch                                       | Hello,          | Yes                 |
| Type `Raffi`                                       | Hello, Raffi    | Yes                 |
| Delete all typed characters                        | Hello,          | Yes                 |
| Type `Dina`, fully terminate the app, and relaunch | Hello,          | Yes                 |

## 5. Current explanation

In your own words, describe the difference between the ordinary state value used
inside `Text("Hello, \(name)")` and the expression supplied to `TextField`.

> all i know is that the first one is a @State wrapper value, and the TextField one is a @Binding wrapper value, idk why it needs to be like that tho, my guess maybe so that it creates this State Binding relationship between each views so that it like transfering the in state memory to another view

## Ready for review

- [ ] I answered and predicted before running.
- [ ] I used the compiler or completion rather than copying a solution.
- [ ] I ran all four observations and preserved any incorrect predictions.

## Tutor review 1

### Demonstrated

- Independently supplied `$name` to `TextField`.
- Built and ran the view successfully.
- Correctly predicted all four complete greeting values.
- Correctly predicted that termination loses the nonpersistent name.

### Value versus binding

`NameEntryView` owns one piece of storage:

```swift
@State private var name = ""
```

The property wrapper provides two related expressions:

| Expression | Type | Purpose |
|---|---|---|
| `name` | `String` | Read or directly mutate the current value inside the owner. |
| `$name` | `Binding<String>` | Give another UI component a get/set connection to that same value. |

`Text` only needs to read a value to construct its description, so interpolation
uses `name`. A `TextField` must display the current text **and write new text back**
as the user types, so its `text:` parameter requires `Binding<String>`.

```text
NameEntryView owns @State storage
              |
              | provides $name
              v
TextField reads current text and writes typed text
              |
              v
@State name changes -> SwiftUI update -> Text reads name
```

There is no second stored string and no memory transfer. `$name` is the projected
binding supplied by `@State`. A custom child view would declare an `@Binding`
property if you later chose to pass this connection into that child, but this probe
does not yet contain a custom child view.

### Understanding check

Complete without running code:

1. What is the type and job of `name`?

   > TODO

2. What is the type and job of `$name`?

   > TODO

3. When the user types `A`, which view owns the storage, and what path causes the
   greeting to change?

   > TODO
