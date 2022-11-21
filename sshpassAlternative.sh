#!/usr/bin/expect
# By damn_c @ stackoverflow
set timeout 20

set cmd [lrange $argv 1 end]
set password [lindex $argv 0]

eval spawn $cmd
expect "password:"
send "$password\r";
interact
