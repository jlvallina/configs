#!/bin/bash

/usr/bin/rclone copy --update --verbose --transfers 30 --checkers 8 --contimeout 60s --timeout 300s --retries 3 --low-level-retries 10 --stats 1s "/home/fofui/Documents" "softlab_drive:LinuxBackup/Documents"
/usr/bin/rclone copy --update --verbose --transfers 30 --checkers 8 --contimeout 60s --timeout 300s --retries 3 --low-level-retries 10 --stats 1s "/home/fofui/Passwords.kdbx" "softlab_drive:LinuxBackup/Credentials"
/usr/bin/rclone copy --update --verbose --transfers 30 --checkers 8 --contimeout 60s --timeout 300s --retries 3 --low-level-retries 10 --stats 1s "/home/fofui/.ssh" "softlab_drive:LinuxBackup/ssh"
/usr/bin/rclone copy --update --verbose --transfers 30 --checkers 8 --contimeout 60s --timeout 300s --retries 3 --low-level-retries 10 --stats 1s "/etc/hosts" "softlab_drive:LinuxBackup/"
