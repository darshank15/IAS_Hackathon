echo "Enter Ip"
read ip
echo "Enter UserName"
read uname
echo "Enter Password"
read pass

sshpass -p "$pass" scp testing.py "$uname"@"$ip":/home/vatsal/Documents/IIIT/Sem-2/IAS/Hackathon/testing.py
# sshpass -p "$pass" scp server.py "$uname"@"$ip":server.py
sshpass -p "$pass" scp script.sh "$uname"@"$ip":/home/vatsal/Documents/IIIT/Sem-2/IAS/Hackathon/script.sh
sshpass -p "$pass" scp model.ckpt.meta "$uname"@"$ip":/home/vatsal/Documents/IIIT/Sem-2/IAS/Hackathon/model.ckpt.meta
sshpass -p "$pass" scp model.ckpt.index "$uname"@"$ip":/home/vatsal/Documents/IIIT/Sem-2/IAS/Hackathon/model.ckpt.index
sshpass -p "$pass" scp model.ckpt.data-00000-of-00001 "$uname"@"$ip":/home/vatsal/Documents/IIIT/Sem-2/IAS/Hackathon/model.ckpt.data-00000-of-00001
sshpass -p "$pass" scp checkpoint "$uname"@"$ip":/home/vatsal/Documents/IIIT/Sem-2/IAS/Hackathon/checkpoint
# sshpass -p "$pass" ssh "$uname"@"$ip"
sleep 5m
wget https://raw.githubusercontent.com/VatsalSoni301/temporary/master/acc.txt