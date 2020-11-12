import string
import random
import csv
from randomtimestamp import randomtimestamp

dataset = []
random.seed(1)

# 1. Generate Meets
m = 5000
meets = []
for i in range(m):
	temp = "https://meet.google.com/"
	for j in range(3):
		temp += random.choice(string.ascii_lowercase)
	temp += '-'
	for j in range(4):
		temp += random.choice(string.ascii_lowercase)
	temp += '-'
	for j in range(3):
		temp += random.choice(string.ascii_lowercase)
	meets.append(temp)

# 2. Generate Emails
n = 500000
emails = []
for i in range(11,21):
	for j in range(int(n/10)):
		temp = ""
		for k in range(i):
			temp += random.choice(string.ascii_lowercase+string.digits)
		temp += "@gmail.com"
		emails.append(temp)
for i in range(n):
	temp = []
	temp.append(emails[i])
	temp.append(meets[random.randint(0, m-1)])
	dataset.append(temp)

# 3. Generate IP address
for i in range(n):
	ip = '{}.{}.{}.{}'.format(*__import__('random').sample(range(0,255),4))
	dataset[i].append(ip)

# 4. Generate Locations
locations = []
f = open("temp.txt","r")
for x in f:
	l = x
	locations.append(l[:-1])
for i in range(n):
	dataset[i].append(locations[random.randint(0, 1000)])

# 5. Generate timestamp
for i in range(n):
    dataset[i].append(randomtimestamp(start_year=1990)[11:])
    dataset[i].append('0')

dataset = sorted(dataset, key=lambda x: x[4])

# 6. Add admin
dic = {}
for i in range(n):
    if dataset[i][1] in dic:
        dataset[i].append('0')
    else:
        dic[dataset[i][1]] = 'true'
        dataset[i].append('1')

# 7. Create wrong participant
for i in range(int(n/1000)):
    l = dataset[random.randint(0,n-1)]
    if l[6] == '1':
        i -= 1
        continue
    l[2] = '{}.{}.{}.{}'.format(*__import__('random').sample(range(0,255),4))
    l[3] = locations[random.randint(0, 1000)]
    dataset.append(l)
    if i%50 == 0:
        l[2] = '{}.{}.{}.{}'.format(*__import__('random').sample(range(0,255),4))
        l[3] = locations[random.randint(0, 1000)]
        dataset.append(l)

# 8. Add earlier participant
for i in range(10):
    index = random.randint(0,n-1)
    if dataset[index][6] != '1':
        i -= 1
        continue
    dataset[index][4] = "00:00:00"

# 8.5 Add device type
devices = ['HP Laptop',
     'Asus Laptop',
     'MSI Laptop',
     'Apple Laptop',
     'Acer Laptop',
     'Dell Laptop',
     'Lenovo Laptop',
     'Microsoft Laptop',
     'Huawei Laptop',
     'Xiaomi Laptop',
     'Samsung Laptop',
     'Micromax Laptop',
     'HCL Laptop',
     'WIPRO Laptop',
     'Reliance Laptop',
     'LG Laptop',
     'Lava Laptop',
     'Sony Laptop',
     'Gateway Laptop',
     'NOTION INK Laptop',
     'Smartron Laptop',
     'Iball Laptop',
     'Toshiba Laptop',
     'Fujitsu Laptop',
     'Acer Mobile',
     'Alcatel Mobile',
     'Allview Mobile',
     'Amazon Mobile',
     'Amoi Mobile',
     'Apple Mobile',
     'AT&T Mobile',
     'Benefon Mobile',
     'Benq Mobile',
     'Benq-Siemens Mobile',
     'Bird Mobile',
     'Blackberry Mobile',
     'BLU Mobile',
     'Bosch Mobile',
     'BQ Mobile',
     'Casio Mobile',
     'CAT Mobile',
     'Celkon Mobile',
     'Chea Mobile',
     'Coolpad Mobile',
     'Dell Mobile',
     'Emporia Mobile',
     'Energizer Mobile',
     'Ericsson Mobile',
     'Eten Mobile',
     'Fairphone Mobile',
     'Fujitsu Siemens Mobile',
     'Garmin-Asus Mobile',
     'Gigabyte mobile',
     'Gionee mobile',
     'Google mobile',
     'Haier mobile',
     'Honor mobile', 
     'HP mobile',
     'HTC mobile',
     'Huawei mobile',
     'I-Mate mobile',
     'I-Mobile mobile',
     'Icemobile mobile',
     'Infinix mobile',
     'Innostream mobile',
     'Inq mobile',
     'Intex mobile',
     'Jolla mobile', 
     'Karbonn mobile', 
     'Kyocera mobile', 
     'Lava mobile',
     'Leeco mobile',
     'Lenovo mobile',
     'Lg mobile',
     'Maxon mobile',
     'Maxwest mobile',
     'Meizu mobile',
     'Micromax mobile',
     'Microsoft mobile',
     'Mitac mobile',
     'Mitsubishi mobile',
     'Modu mobile',
     'Motorola mobile',
     'Mwg mobile',
     'Nec mobile',
     'Neonode mobile',
     'Niu mobile',
     'Nokia mobile',
     'Nvidia mobile',
     'O2 mobile',
     'Oneplus mobile',
     'Oppo mobile',
     'Orange mobile',
     'Palm mobile',
     'Panasonic mobile',
     'Pantech mobile',
     'Parla mobile',
     'Philips mobile',
     'Plum mobile',
     'Posh mobile',
     'Prestigio mobile',
     'Qmobile mobile',
     'Qtek mobile',
     'Razer mobile',
     'Realme mobile',
     'Sagem mobile',
     'Samsung mobile',
     'Sendo mobile',
     'Sewon mobile',
     'Sharp mobile',
     'Siemens mobile',
     'Sonim mobile',
     'Sony mobile',
     'Sony Ericsson mobile',
     'Spice mobile',
     'T-Mobile mobile',
     'Tcl mobile',
     'Tecno mobile',
     'Tel.Me. mobile',
     'Telit mobile',
     'Thuraya mobile',
     'Toshiba mobile',
     'Ulefone mobile',
     'Unnecto mobile',
     'Vertu mobile',
     'Verykool mobile',
     'Vivo mobile',
     'Vk Mobile mobile',
     'Vodafone mobile',
     'Wiko mobile',
     'Wnd mobile',
     'Xcute mobile',
     'Xiaomi mobile',
     'Xolo mobile',
     'Yezz mobile',
     'Yota mobile',
     'Yu mobile',
     'Zte Device mobile'
     ]
for i in range(len(dataset)):
    dataset[i].append(devices[random.randint(0,len(devices)-1)])

# 9. Add leaving entries
count = 0
n = len(dataset)
for i in range(n):
    l = []
    for x in dataset[i]:
        l.append(x)
    l[5] = '1'
    if l[6] == '1':
        l[4] = "23:59:59"
    elif l[4] > "23:00:00":
        count += 1
        continue
    else:
        temp = l[4]
        temp1 = randomtimestamp(start_year=1990)[11:]
        while temp >= temp1:
            temp1 = randomtimestamp(start_year=1990)[11:]
        l[4] = temp1
    dataset.append(l)

dataset = sorted(dataset, key=lambda x: x[4])

# 10. Write to csv
file = open('dataset.csv', 'a+', newline='')
with file:
    write = csv.writer(file)
    write.writerows(dataset)

















