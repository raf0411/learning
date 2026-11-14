# Read-only service investigation — 2026-11-14

Use your Ubuntu VM. Do not start, stop, restart, enable, disable, or edit any service. No sudo is required for this task; record access limitations instead of changing permissions.

## 1. Choose a service

List running services:

```bash
systemctl list-units --type=service --state=running --no-pager
```

Choose one service other than cron. Copy its exact unit name:

dbus.service

## 2. Collect evidence

Choose your own commands, using local documentation if needed:

- Inspect its current status with full, untruncated lines.
- Display its service definition and any displayed overrides.
- Request its last **five journal entries from the current boot**.

Record each command and its actual output below. No entries or an access warning is a valid observation; do not invent missing evidence.

```text
raf_0411@ubuntu-desktop:~$ systemctl --no-pager --full status dbus.service
● dbus.service - D-Bus System Message Bus
     Loaded: loaded (/usr/lib/systemd/system/dbus.service; static)
     Active: active (running) since Sat 2026-11-14 11:37:54 UTC; 53min ago
 Invocation: abb80e6c2a7448b287780093830a0ea2
TriggeredBy: ● dbus.socket
       Docs: man:dbus-daemon(1)
   Main PID: 1105 (dbus-daemon)
      Tasks: 1 (limit: 2264)
     Memory: 5.5M (peak: 7.8M)
        CPU: 865ms
     CGroup: /system.slice/dbus.service
             └─1105 @dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only

Nov 14 11:43:01 ubuntu-desktop dbus-daemon[1105]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.14' (uid=0 pid=1125 comm="/usr/lib/snapd/snapd" label="unconfined")
Nov 14 11:43:01 ubuntu-desktop dbus-daemon[1105]: [system] Successfully activated service 'org.freedesktop.timedate1'
Nov 14 11:46:14 ubuntu-desktop dbus-daemon[1105]: [system] Activating via systemd: service name='org.freedesktop.fwupd' unit='fwupd.service' requested by ':1.118' (uid=982 pid=4874 comm="/usr/bin/fwupdmgr refresh" label="unconfined")
Nov 14 11:46:14 ubuntu-desktop dbus-daemon[1105]: [system] Activating via systemd: service name='org.bluez' unit='dbus-org.bluez.service' requested by ':1.120' (uid=0 pid=4883 comm="/usr/libexec/fwupd/fwupd" label="unconfined")
Nov 14 11:46:16 ubuntu-desktop dbus-daemon[1105]: [system] Successfully activated service 'org.freedesktop.fwupd'
Nov 14 11:46:39 ubuntu-desktop dbus-daemon[1105]: [system] Failed to activate service 'org.bluez': timed out (service_start_timeout=25000ms)
Nov 14 11:56:30 ubuntu-desktop dbus-daemon[1105]: [system] Activating via systemd: service name='net.reactivated.Fprint' unit='fprintd.service' requested by ':1.81' (uid=1000 pid=3611 comm="/usr/bin/gnome-shell --mode=ubuntu" label="unconfined")
Nov 14 11:56:30 ubuntu-desktop dbus-daemon[1105]: [system] Successfully activated service 'net.reactivated.Fprint'
Nov 14 12:02:24 ubuntu-desktop dbus-daemon[1105]: [system] Activating via systemd: service name='net.reactivated.Fprint' unit='fprintd.service' requested by ':1.81' (uid=1000 pid=3611 comm="/usr/bin/gnome-shell --mode=ubuntu" label="unconfined")
Nov 14 12:02:24 ubuntu-desktop dbus-daemon[1105]: [system] Successfully activated service 'net.reactivated.Fprint'
raf_0411@ubuntu-desktop:~$ journalctl -u dbus.service -b -n 5 --no-pager
Nov 14 11:46:39 ubuntu-desktop dbus-daemon[1105]: [system] Failed to activate service 'org.bluez': timed out (service_start_timeout=25000ms)
Nov 14 11:56:30 ubuntu-desktop dbus-daemon[1105]: [system] Activating via systemd: service name='net.reactivated.Fprint' unit='fprintd.service' requested by ':1.81' (uid=1000 pid=3611 comm="/usr/bin/gnome-shell --mode=ubuntu" label="unconfined")
Nov 14 11:56:30 ubuntu-desktop dbus-daemon[1105]: [system] Successfully activated service 'net.reactivated.Fprint'
Nov 14 12:02:24 ubuntu-desktop dbus-daemon[1105]: [system] Activating via systemd: service name='net.reactivated.Fprint' unit='fprintd.service' requested by ':1.81' (uid=1000 pid=3611 comm="/usr/bin/gnome-shell --mode=ubuntu" label="unconfined")
Nov 14 12:02:24 ubuntu-desktop dbus-daemon[1105]: [system] Successfully activated service 'net.reactivated.Fprint'
raf_0411@ubuntu-desktop:~$ systemctl --no-pager cat dbus.service
# /usr/lib/systemd/system/dbus.service
[Unit]
Description=D-Bus System Message Bus
Documentation=man:dbus-daemon(1)
Requires=dbus.socket
# Do not stop on shutdown
DefaultDependencies=no
Wants=sysinit.target
After=sysinit.target basic.target

[Service]
Type=notify
NotifyAccess=main
ExecStart=@/usr/bin/dbus-daemon @dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
ExecReload=/usr/bin/dbus-send --print-reply --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig
OOMScoreAdjust=-900
User=messagebus
Group=messagebus
AmbientCapabilities=CAP_AUDIT_WRITE
raf_0411@ubuntu-desktop:~$ 
```

## 3. Interpret the evidence

Keep each answer to one or two sentences. If an unfamiliar field prevents a conclusion, identify it rather than guessing.

1. What is the service's current runtime state, and what startup-enablement state is reported? Explain why these describe different things.

Loaded: loaded, Active: active (running)

2. What command does its definition configure systemd to launch, and what main PID, if any, is reported in its status?

main PID: 1105, command:@/usr/bin/dbus-daemon @dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only

3. State one claim supported by the journal entries and one outcome those entries do **not** establish.

idk

Documentation or hints used:

None
