import re
list_keyword = ['cetak', 'kelas', 'Integer', 'Float',
                'String', 'Char', 'Public', 'Privat', 'Terproteksi', 'Konstan']

list_alp = [chr(x) for x in range(97,123)]+[chr(x).upper() for x in range(97,123)]
list_angka = [str(x) for x in range(0,10)] # angka
list_operator_a= ["+", "*", "-", "/", "%"] #operator aritmatik
list_operator_rel = ["<", "=", "!", ">", "="] #operator relasi/perbandingan
list_operator_log = ["!!", "||", "&&"] #operator logika
list_operator_u = []
unused_punc = [" ", "\n",]
unknown_op = ["&"]

def tokenizing(str_):
    token = []
    current_token = ""
    num_zone = False
    str_zone = False
    opa_zone = False
    opl_zone = False
    opr_zone = False
    opr_count = 0
    opl_count = 0
    temp_opa = ""
    temp_opl = ""
    temp_opr = ""
    temp_num = ""
    temp_string = ""


    for t in str_+"a":
        current_token += t
        eval_count = int(str_zone+num_zone) #jika terjadi kasus dimana str_zone dan num_zone == True, dapat dicegah dengan variable ini
        #deprecated : eval_count if eval_count-1 > 0 else eval_count+1

        for i in range(4):

            if current_token == "": #mengecek apakah ada "" di dalam current_token
                pass
            elif current_token in list_keyword and str_zone == False: #mengecek apakah ada list_keyword pada daerah non string
                token.append("KEYWORD:"+current_token)
                current_token = ""

            #khusus angka dan operator
            elif current_token in list_angka and str_zone == False and num_zone == False: #mengecek apakah ada angka pada daerah non string
                num_zone = True
                temp_num+=current_token
                current_token = ""
                if temp_opr != "" and opr_zone == True:
                    token.append("OP_REL:"+temp_opr)
                    temp_opr = ""
                    opr_zone = False

            elif current_token in list_angka and str_zone == False and num_zone == True:
                temp_num+=current_token
                current_token = ""

            elif (current_token not in list_angka) and str_zone == False and num_zone == True:
                num_zone = False
                token.append("NUM:" + temp_num)
                temp_num = ""


            #untuk operator aritmatik
            elif current_token in list_operator_a and str_zone == False:
                token.append("OP_A:" + current_token)
                current_token = ""

            #untuk operator relasi
            elif current_token in list_operator_rel and str_zone == False and opr_zone == False:
                opr_zone = True
                temp_opr+=current_token
                current_token = ""

            elif current_token in list_operator_rel and str_zone == False and opr_zone == True:
                temp_opr+=current_token
                current_token = ""

            elif current_token not in list_operator_rel and str_zone == False and opr_zone == True:
                token.append("OP_REL:" + temp_opr)
                temp_opr = ""
                opr_zone = False

            #untuk operator logika
            elif current_token in list_operator_log and str_zone == False and opl_zone == False:
                opl_zone = True
                temp_opl+=current_token
                current_token = ""

            elif current_token in list_operator_log and str_zone == False and opl_zone == True:
                temp_opl+=current_token
                current_token = ""

            elif current_token not in list_operator_log and str_zone == False and opl_zone == True:
                token.append("OP_LOG:" + temp_opl)
                temp_opl = ""
                opl_zone = False

            #khusus string atau pungtuasi/separator

            elif current_token in unused_punc and str_zone == False: #mengecek apakah ada token yang tidak diperlukan
                current_token = ""

            elif current_token == " " and str_zone == True: #mengecek apakah ada spasi di daerah string
                pass
            elif "\"" in current_token and str_zone == False: #mengecek apakah ada kutip dua non literal pengawal string saat di zona string
                current_token = ""
                temp_string+="STRING:"
                str_zone = True

            elif "\\\"" in current_token and str_zone == True: #mengecek apakah ada kutip dua literal di daerah string
                temp_string+=current_token.replace("\\\"","\"")
                current_token = ""

            elif "\"" in current_token and str_zone == True: #mengecek apakah ada kutip dua non literal pengakhir string saat di zona string
                temp_string+=current_token[0:-1]
                current_token = ""
                token.append(temp_string)
                temp_string = ""
                str_zone = False










    print(token)



tokenizing(open("test.txt","r").read())
