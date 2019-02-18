echo "Enter Ip"
read ip
echo "Enter UserName"
read uname
echo "Enter Password"
read pass

sshpass -p "$pass" scp testing.py "$uname"@"$ip":testing.py
# sshpass -p "$pass" scp server.py "$uname"@"$ip":server.py
sshpass -p "$pass" scp script.sh "$uname"@"$ip":script.sh
sshpass -p "$pass" scp model.ckpt.meta "$uname"@"$ip":model.ckpt.meta
sshpass -p "$pass" scp model.ckpt.index "$uname"@"$ip":model.ckpt.index
sshpass -p "$pass" scp model.ckpt.data-00000-of-00001 "$uname"@"$ip":model.ckpt.data-00000-of-00001
sshpass -p "$pass" scp checkpoint "$uname"@"$ip":checkpoint
# sshpass -p "$pass" ssh "$uname"@"$ip"
sleep 5m
wget https://raw.githubusercontent.com/VatsalSoni301/temporary/master/acc.txt