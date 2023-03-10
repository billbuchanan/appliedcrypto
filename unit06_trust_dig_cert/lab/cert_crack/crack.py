import OpenSSL 
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from os import listdir

str="fred.pfx"
passwords=["ankle","battery","password","p@55w0rd","password1","bill",'123456','11111','123456',
'12345',
'123456789',
'password',
'iloveyou',
'princess',
'1234567',
'rockyou',
'12345678',
'abc123',
'nicole',
'daniel',
'babygirl',
'monkey',
'lovely',
'jessica',
'654321',
'michael',
'ashley',
'qwerty',
'111111',
'iloveu',
'000000',
'michelle',
'tigger',
'sunshine',
'chocolate',
'password1',
'soccer',
'anthony',
'friends',
'butterfly',
'purple',
           'apple', 'apples', 'apricot', 'apricots', 'avocado', 'avocados', 'banana', 'bananas', 'blackberry', 'blackberries', 
          'blueberry', 'blueberries', 'boysenberry', 'boysenberries', 'cantaloupe', 'cantaloupes', 'Carambola', 'cherry', 'cherries', 
          'coconut', 'coconuts', 'cranberry', 'cranberries', 'date', 'dates', 'dragonfruit', 'dragonfruits', 'elderberry', 
          'elderberries', 'fig', 'figs', 'grape', 'grapes', 'grapefruit', 'grapefruits', 'guava', 'guavas', 'honeydew', 
          'honeydews', 'jackfruit', 'jackfruits', 'kiwi', 'kiwis', 'kumquat', 'kumquats', 'lemon', 'lemons', 'lime', 
          'limes', 'lychee', 'lychees', 'mango', 'mangoes', 'mandarin', 'mandarins', 'nectarine', 'nectarines', 'orange', 
          'oranges', 'papaya', 'papayas', 'peach', 'peaches', 'pear', 'pears', 'persimmon', 'persimmons', 'pineapple', 
          'pineapples', 'plum', 'plums', 'pomegranate', 'pomegranates', 'raspberry', 'raspberries', 'redcurrant', 
          'redcurrants', 'strawberry', 'strawberries', 'tangerine', 'tangerines', 'watermelon', 'watermelons','Aberdeen', 
          'Airdrie', 'Alexandria', 'Alloa', 'Arbroath', 'Ayr', 'Barrhead', 'Bathgate', 'Bearsden', 'Bellshill', 
         'Bishopbriggs', 'Blantyre', 'Bonnyrigg', 'Broxburn', 'Buckhaven', 'Burntisland', 'Cambuslang', 'Carluke', 'Clydebank', 
         'Coatbridge', 'Cumbernauld', 'Cupar', 'Dalgety Bay', 'Dalkeith', 'Dumbarton', 'Dunbar', 'Dunblane', 'Dundee', 
         'Dunfermline', 'Dunoon', 'Duns', 'East Kilbride', 'Edinburgh', 'Elgin', 'Erskine', 'Falkirk', 'Fochabers', 
         'Forfar', 'Forres', 'Girvan', 'Glasgow', 'Glenrothes', 'Gourock', 'Grangemouth', 'Greenock', 'Hamilton', 
         'Hawick', 'Helensburgh', 'Inverness', 'Inverurie', 'Irvine', 'Johnstone', 'Kelso', 'Kilmarnock', 'Kilwinning', 
         'Kinghorn', 'Kingskettle', 'Kirkcaldy', 'Kirkintilloch', 'Kirkwall', 'Lanark', 'Largs', 'Larkhall', 'Lerwick', 
         'Leven', 'Linlithgow', 'Livingston', 'Loanhead', 'Lochgelly', 'Macduff', 'Methil', 'Montrose', 'Motherwell', 
         'Musselburgh', 'Nairn', 'Newton Mearns', 'North Berwick', 'Oban', 'Paisley', 'Penicuik', 'Perth', 'Peterhead', 
         'Pitlochry', 'Prestwick', 'Renfrew', 'Rosyth', 'Rothesay', 'Rutherglen', 'Saltcoats', 'Selkirk', 'Shotts', 
         'St Andrews', 'Stenhousemuir', 'Stevenston', 'Stirling', 'Stonehaven', 'Stornoway', 'Stranraer', 'Tain', 
         'Tayport', 'Tullibody', 'Uddingston', 'Westhill', 'Wick', 'Wishaw','Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia',
             'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 
             'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 
             'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 
             'Comoros', 'Congo, Democratic Republic of the', 'Congo, Republic of the', 'Costa Rica', 'Cote d\'Ivoire', 'Croatia', 
             'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 
             'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 
             'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 
             'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 
             'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 
             'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 
             'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 
             'Micronesia, Federated States of', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 
             'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'North Macedonia', 
             'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 
             'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 
             'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands',
             'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 
             'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago',
             'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States of America',
             'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City (Holy See)', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']



files = listdir()

for file in files:
    if file.split('.')[1] == 'pfx':
        print(f'Attempting to crack the password of {file}')
        for password in passwords:
            try:                
                pfx = open(file, 'rb').read()                
                p12 = OpenSSL.crypto.load_pkcs12(pfx, password)
                print(f'Found: {password}')
            except:
                try:
                    p12 = OpenSSL.crypto.load_pkcs12(pfx, password.lower())
                    print(f'Found: {password}')
                except:
                    try:
                        p12 = OpenSSL.crypto.load_pkcs12(pfx, password.upper())
                        print(f'Found: {password}')
                    except:
                        pass
            # break
                # privkey = OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, p12.get_privatekey())
                # cert = OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, p12.get_certificate())
                # cert = x509.load_pem_x509_certificate(cert, default_backend())

                # print(" Issuer: ",cert.issuer)
                # print(" Subect: ",cert.subject)
                # print(" Serial number: ",cert.serial_number)
                # print(" Hash: ",cert.signature_hash_algorithm.name)
                # print(privkey)
                # print(certificate)
                
            # except:
            #     pass
                # print(f'{file} password is not {password}')
