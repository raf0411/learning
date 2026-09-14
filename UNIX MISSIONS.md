# 1. 🗂 Filesystem

**Commands covered:** `pwd`, `ls`, `cd`, `mkdir`, `cp`, `mv`, `rm`

### Mission 1 — Wrong Server, Wrong Folder

**Difficulty:** ★☆☆☆☆

**Type:** Multiple Choice

**Introduces:** `pwd`

**Scenario:**

You just SSH'd into a production server. Before running a deployment script, you need to make sure you're actually inside the expected directory.

**Objective:**

Display your current working directory.

**Choices:**

- `ls`
- `pwd` ✅
- `cd`
- `find`

**Developer validation:** `pwd`

---

### Mission 2 — Find the Release

**Difficulty:** ★☆☆☆☆

**Type:** Arranging Commands

**Introduces:** `ls`

**Scenario:**

The CI/CD pipeline uploaded a new application build into `/opt/releases`. You need to see which releases are available.

**Objective:**

Navigate to the releases directory and list its contents.

**Command cards:**

- `ls`
- `cd /opt/releases`

**Correct order:**

```
cd /opt/releases
ls
```

This already reuses `cd` conceptually before its dedicated challenge, but Mission 3 makes the player type it themselves.

---

### Mission 3 — Enter the Application Directory

**Difficulty:** ★☆☆☆☆

**Type:** Fill in Command

**Introduces:** `cd`

**Scenario:**

Your backend application is stored in `/srv/payment-api`. You need to enter the application directory before deploying it.

**Objective:**

Move into `/srv/payment-api`.

**Developer validation:**

```bash
cd /srv/payment-api
```

---

### Mission 4 — Prepare a Rollback Directory

**Difficulty:** ★★☆☆☆

**Type:** Arranging Commands

**Introduces:** `mkdir`

**Reuses:** `cd`

**Scenario:**

Before deploying a new version, your team requires a directory for rollback files.

**Objective:**

Enter the application folder, then create a directory called `rollback`.

**Command cards:**

```
mkdir rollback
cd /srv/payment-api
```

**Correct order:**

```bash
cd /srv/payment-api
mkdir rollback
```

---

### Mission 5 — Backup Configuration

**Difficulty:** ★★☆☆☆

**Type:** Fill in Command

**Introduces:** `cp`

**Reuses:** `ls`

**Scenario:**

You're about to modify the production configuration. Company policy says you must create a backup first.

Current files include:

```
app.conf
rollback/
```

**Objective:**

Copy `app.conf` into the `rollback` directory as `app.conf.bak`.

**Developer validation:**

```bash
cp app.conf rollback/app.conf.bak
```

Optional second step:

```bash
ls rollback
```

---

### Mission 6 — Promote the New Release

**Difficulty:** ★★★☆☆

**Type:** Arranging Commands

**Introduces:** `mv`

**Reuses:** `ls`

**Scenario:**

The deployment pipeline extracted a folder called:

```
payment-api-new
```

It now needs to become:

```
payment-api-current
```

**Objective:**

Check that the new folder exists, then rename it.

**Command cards:**

```
mv payment-api-new payment-api-current
ls
```

**Correct order:**

```bash
ls
mv payment-api-new payment-api-current
```

---

### Mission 7 — Clean a Failed Deployment

**Difficulty:** ★★★★☆

**Type:** Fill in Commands

**Introduces:** `rm`

**Reuses:** `pwd`, `cd`, `ls`

**Scenario:**

A failed CI/CD run left `broken-release.tar.gz` inside `/opt/releases`.

You have been asked to remove **only that file**.

**Objective:**

Verify where you are, enter the releases directory, inspect it, and remove the failed artifact.

**Expected sequence:**

```bash
pwd
cd /opt/releases
ls
rm broken-release.tar.gz
```

This becomes the **Filesystem section capstone**.

---

# 2. 🔍 Inspecting Systems

**Commands covered:** `cat`, `less`, `head`, `tail`, `grep`, `find`

### Mission 8 — Check Application Configuration

**Difficulty:** ★☆☆☆☆

**Type:** Multiple Choice

**Introduces:** `cat`

**Scenario:**

Your application is connecting to the wrong API environment. The configuration file is small, so you want to quickly display it.

**Objective:**

Display `/etc/payment-api/app.conf`.

**Choices:**

```
cat /etc/payment-api/app.conf
less /etc/payment-api/app.conf
find /etc/payment-api/app.conf
cd /etc/payment-api/app.conf
```

**Correct:** `cat /etc/payment-api/app.conf`

---

### Mission 9 — Investigate a Huge Log File

**Difficulty:** ★★☆☆☆

**Type:** Fill in Command

**Introduces:** `less`

**Scenario:**

`application.log` contains hundreds of thousands of lines. Printing everything to the terminal would be inconvenient.

**Objective:**

Open the log so you can navigate through it page by page.

**Developer validation:**

```bash
less application.log
```

For your simulator, you don't need to fully emulate `less`; you can simply show a scrollable/paged log screen.

---

### Mission 10 — Inspect Startup Logs

**Difficulty:** ★★☆☆☆

**Type:** Arranging Command Pieces

**Introduces:** `head`

**Scenario:**

The application crashes during startup. The beginning of the log contains initialization information.

**Objective:**

Display the first 20 lines of `application.log`.

**Pieces:**

```
head
-n 20
application.log
```

**Correct:**

```bash
head -n 20 application.log
```

---

### Mission 11 — Check the Latest Logs

**Difficulty:** ★★☆☆☆

**Type:** Fill in Command

**Introduces:** `tail`

**Scenario:**

A user just reported an API error. You don't care about yesterday's logs—you need the most recent entries.

**Objective:**

Display the last 50 lines of `application.log`.

**Developer validation:**

```bash
tail -n 50 application.log
```

---

### Mission 12 — Hunt for Errors

**Difficulty:** ★★★☆☆

**Type:** Arranging Commands

**Introduces:** `grep`

**Reuses:** `tail`

**Scenario:**

The latest application logs contain hundreds of entries. You're specifically looking for lines containing `ERROR`.

**Objective:**

First inspect recent logs, then search the log for errors.

**Command cards:**

```
grep "ERROR" application.log
tail -n 50 application.log
```

**Correct order:**

```bash
tail -n 50 application.log
grep "ERROR" application.log
```

Later, when you teach pipes, this could evolve into:

```bash
tail -n 50 application.log | grep "ERROR"
```

But I would **not require pipes in your MVP yet**.

---

### Mission 13 — Find the Missing Configuration

**Difficulty:** ★★★★☆

**Type:** Fill in Commands

**Introduces:** `find`

**Reuses:** `grep`

**Scenario:**

A service is using the wrong database server, but nobody remembers where its configuration file is stored.

You know the file is called:

```
database.conf
```

and should exist somewhere under `/etc`.

**Objective:**

Find the configuration file, then search it for `database_host`.

**Expected sequence:**

```bash
find /etc -name "database.conf"
grep "database_host" /etc/payment-api/database.conf
```

This is the **system inspection capstone**.

---

# 3. 🔐 Permissions

**Commands covered:** `chmod`, `chown`

### Mission 14 — Deployment Script Won't Run

**Difficulty:** ★★☆☆☆

**Type:** Multiple Choice

**Introduces:** `chmod`

**Scenario:**

Your deployment script exists:

```
deploy.sh
```

but running it results in:

```
Permission denied
```

The file needs execute permission.

**Which command should you use?**

- `chown deploy.sh`
- `chmod +x deploy.sh` ✅
- `rm deploy.sh`
- `cat deploy.sh`

**Developer validation:**

```bash
chmod +x deploy.sh
```

---

### Mission 15 — Fix Web Server Ownership

**Difficulty:** ★★★★☆

**Type:** Fill in Commands

**Introduces:** `chown`

**Reuses:** `chmod`, `ls`

**Scenario:**

A deployment was accidentally performed as `root`.

The web directory now belongs to the wrong user, and the web server cannot access it properly.

The application should belong to:

```
www-data:www-data
```

**Objective:**

Inspect the directory, fix its ownership, and make the directory accessible.

**Expected sequence:**

```bash
ls -l /var/www/app
chown -R www-data:www-data /var/www/app
chmod 755 /var/www/app
```

---

# 4. ⚙️ Processes

**Commands covered:** `ps`, `top`, `kill`

### Mission 16 — Is the API Actually Running?

**Difficulty:** ★★☆☆☆

**Type:** Multiple Choice

**Introduces:** `ps`

**Scenario:**

Monitoring reports that the API may have stopped.

You want a snapshot of the processes currently running on the server.

**Choices:**

- `ps aux` ✅
- `pwd`
- `ping`
- `chmod`

**Developer validation:**

```bash
ps aux
```

---

### Mission 17 — CPU Usage Is at 100%

**Difficulty:** ★★★☆☆

**Type:** Multiple Choice

**Introduces:** `top`

**Scenario:**

Your monitoring dashboard reports that CPU usage suddenly jumped to 100%.

You need a continuously updating view of running processes.

**Choices:**

- `cat`
- `top` ✅
- `find`
- `curl`

**Developer validation:**

```bash
top
```

Your simulation can display fake processes with one process consuming something like `95% CPU`.

---

### Mission 18 — Stop the Broken Worker

**Difficulty:** ★★★★★

**Type:** Fill in Commands

**Introduces:** `kill`

**Reuses:** `ps`, `grep`

**Scenario:**

A background worker is stuck and consuming excessive CPU.

You need to locate the process called:

```
payment-worker
```

The simulated output tells the player its PID is:

```
4821
```

**Objective:**

Locate the process, terminate it, then verify it is gone.

**Expected sequence:**

```bash
ps aux
grep "payment-worker"
kill 4821
ps aux
```

Later you could teach:

```bash
ps aux | grep payment-worker
```

But again, that can wait until you add shell operators.

---

# 5. 🌐 Networking

**Commands covered:** `ping`, `curl`, `ssh`, `ss`

### Mission 19 — Can the Server Be Reached?

**Difficulty:** ★★☆☆☆

**Type:** Multiple Choice

**Introduces:** `ping`

**Scenario:**

Application Server A suddenly cannot communicate with Application Server B at:

```
10.0.0.20
```

Before investigating the application itself, check basic network connectivity.

**Correct command:**

```bash
ping 10.0.0.20
```

Possible choices:

- `curl 10.0.0.20`
- `ping 10.0.0.20` ✅
- `ssh localhost`
- `ps 10.0.0.20`

---

### Mission 20 — Check the API Health Endpoint

**Difficulty:** ★★☆☆☆

**Type:** Fill in Command

**Introduces:** `curl`

**Scenario:**

The server responds to the network, but users still say the API is down.

The API exposes:

```
<http://localhost:8080/health>
```

**Objective:**

Make an HTTP request to the health endpoint.

**Developer validation:**

```bash
curl <http://localhost:8080/health>
```

Your simulated response could be:

```json
{"status":"healthy"}
```

---

### Mission 21 — Investigate the Remote Server

**Difficulty:** ★★★☆☆

**Type:** Arranging Command Pieces

**Introduces:** `ssh`

**Scenario:**

The application works on one server but fails on another.

You need to connect to:

```
10.0.0.20
```

using the account:

```
deploy
```

**Pieces:**

```
ssh
deploy@
10.0.0.20
```

**Correct command:**

```bash
ssh deploy@10.0.0.20
```

---

### Mission 22 — Why Isn't Port 8080 Working?

**Difficulty:** ★★★★★

**Type:** Fill in Commands

**Introduces:** `ss`

**Reuses:** `ssh`, `curl`

**Scenario:**

Monitoring reports:

```
payment-api is unreachable on port 8080
```

The machine itself is reachable.

You need to remotely investigate whether anything is listening on the application's port and whether the API responds locally.

**Expected sequence:**

```bash
ssh deploy@10.0.0.20
ss -ltnp
curl <http://localhost:8080/health>
```

Simulated `ss` output could reveal:

```
LISTEN ... 0.0.0.0:8080
```

or intentionally show **no port 8080**, depending on the mission.

This becomes a much more realistic troubleshooting problem because the player has to understand:

**network reachable ≠ application reachable.**

---

# 6. 📦 Logs & Services

**Commands covered:** `journalctl`, `systemctl`

### Mission 23 — Why Did the Service Crash?

**Difficulty:** ★★★☆☆

**Type:** Arranging Command Pieces

**Introduces:** `journalctl`

**Scenario:**

The `payment-api` service crashed shortly after a deployment.

You need to inspect its system logs.

**Pieces:**

```
journalctl
-u
payment-api
```

**Correct command:**

```bash
journalctl -u payment-api
```

A harder variant could later become:

```bash
journalctl -u payment-api -n 50
```

---

### Mission 24 — Production API Is Down

**Difficulty:** ★★★★★

**Type:** Fill in Commands

**Introduces:** `systemctl`

**Reuses:** `journalctl`

This should be one of your **final MVP missions**.

**Scenario:**

Monitoring alerts:

```
CRITICAL
payment-api is DOWN
```

Customers are receiving:

```
503 Service Unavailable
```

You have SSH access to the server.

Your job is to investigate the service, find the problem, restart it, and verify that it recovered.

**Objective:**

First check the service state.

Then inspect its logs.

Then restart the service.

Finally verify that it is running.

**Expected sequence:**

```bash
systemctl status payment-api
journalctl -u payment-api -n 50
systemctl restart payment-api
systemctl status payment-api
```

Your simulated logs could contain something like:

```
ERROR: Failed to connect to database
payment-api.service: Failed with result 'exit-code'
```

After the restart, simulated output:

```
Active: active (running)
```

That feels much closer to an actual junior Sysadmin/DevOps incident than a question like **"What does systemctl do?"**

---