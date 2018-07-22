import re

pat_alp = re.compile("[A-Za-z]")#[chr(x) for x in range(97,123)]+[chr(x).upper() for x in range(97,123)]
pat_al_ident_start = re.compile("[A-Za-z_]")
pat_opa = re.compile(r"[-\+\*/%]")
pat_angka = re.compile("[0-9]") # angka
pat_allowed_ident = re.compile("[A-Za-z0-9_]")
#pat_unused_punc = re.compile("[\s]")
list_operator_a= ["+", "*", "-", "/", "%"] #operator aritmatik
list_operator_rel = ["<", "=", "!", ">", "="] #operator relasi/perbandingan
list_operator_log = ["!!", "||", "&&"] #operator logika
keyword = ['cetak', 'kelas']




def tokenizing(str_):

    token = []
    current_token = ""
    num_zone = False
    str_zone = False
    opa_zone = False
    opl_zone = False
    opr_zone = False
    ident_zone = False
    slash_state = False
    end_str = False
    temp_slash = ""
    temp_opa = ""
    temp_opl = ""
    temp_opr = ""
    temp_num = ""
    temp_ident = ""
    temp_string = ""

    for i in range(len(str_+" ")-1):
        t = str_[i]
        current_token+=t

        #evaluasi identifier dan keyword
        for j in range(1):

            if current_token == "":
                pass

            # elif re.match("\n", current_token) and str_zone == False:
            #     token.append(current_token)

            elif re.match(r"\s",current_token) and str_zone == False:
                current_token = ""
                if num_zone == True and temp_num != "":
                    token.append("NUM:"+ temp_num)
                    temp_num = ""
                    num_zone = False

                if ident_zone == True and temp_ident != "":
                    if temp_ident in keyword:
                        token.append("KEYW:" + temp_ident)
                    else:
                        token.append("IDENT:" + temp_ident)
                    temp_ident = ""
                    ident_zone = False

                if opa_zone == True and temp_opa != "":
                    token.append("OP_A:"+temp_opa)
                    temp_opa = ""
                    opa_zone = False



            elif re.match(r"\n", current_token) and str_zone == False:
                token.append("PUNC:"+current_token)
                current_token = ""

            # evaluasi identifier
            elif re.match(pat_al_ident_start,current_token) and num_zone == False and str_zone == False and opr_zone == False and opl_zone == False and opa_zone == False and ident_zone == False:
                temp_ident+=current_token
                current_token = ""
                ident_zone = True

            elif re.match(pat_allowed_ident,current_token) and num_zone == False and str_zone == False and opr_zone == False and opl_zone == False and opa_zone == False and ident_zone == True:
                temp_ident+=current_token
                current_token = ""

            elif not re.match(pat_allowed_ident,current_token) and num_zone == False and str_zone == False and opr_zone == False and opl_zone == False and opa_zone == False and ident_zone == True:
                if temp_ident in keyword:
                    token.append("KEYW:"+temp_ident)
                else:
                    token.append("IDENT:"+temp_ident)
                temp_ident = ""
                ident_zone = False

                #evaluasi operator aritmatik
                if re.match(r"[\*+-/]", current_token) and opa_zone == False:
                    temp_opa+=current_token
                    current_token = ""
                    opa_zone = True

            #evaluasi angka
            elif re.match(pat_angka,current_token) and num_zone == False and str_zone == False and opr_zone == False and opl_zone == False and opa_zone == False and ident_zone == False:
                temp_num+=current_token
                current_token = ""
                num_zone = True

            elif re.match(pat_angka,current_token) and num_zone == True and str_zone == False and opr_zone == False and opl_zone == False and opa_zone == False and ident_zone == False:
                temp_num+=current_token
                current_token = ""


            elif not re.match(pat_angka,current_token) and num_zone == True and str_zone == False and opr_zone == False and opl_zone == False and opa_zone == False and ident_zone == False:
                token.append("NUM:"+temp_num)
                temp_num = ""
                num_zone = False

                #evaluasi string
                if re.match(r"\"", current_token) and str_zone == False:
                    current_token = ""
                    str_zone = True

                #evaluasi operator aritmatik
                if re.match(pat_opa, current_token) and num_zone == False and str_zone == False and opr_zone == False and opl_zone == False and opa_zone == False and ident_zone == False:
                    temp_opa += current_token
                    current_token = ""
                    opa_zone = True


                #evaluasi identifier
                if re.match(pat_al_ident_start,current_token) and ident_zone == False:
                    temp_ident+=current_token
                    ident_zone = True
                    current_token = ""



            #evaluator string1

            elif re.match(r"\"", current_token) and num_zone == False and str_zone == False and opr_zone == False and opl_zone == False and opa_zone == False and ident_zone == False:
                current_token = ""
                str_zone = True

            elif (re.match(r"\"", current_token) or re.match(r"\\",current_token)) and re.match(r"\\", temp_slash) and str_zone == True:
                temp_string+="\\"+current_token
                temp_slash = ""
                current_token = ""

            elif re.match(r"\\", current_token) and str_zone == True:
                temp_slash+=current_token
                current_token = ""

            elif re.match(r"[^\\\"]", current_token) and str_zone == True:
                temp_string+=current_token
                current_token = ""

            elif re.match(r"\"", current_token) and str_zone == True:
                token.append("STRING:"+temp_string)
                temp_string = ""
                current_token = ""
                str_zone = False



            # elif re.match("[^\\\"]",current_token) and str_zone == True:
            #     temp_string+=current_token
            #     current_token = ""

            #evaluasi operator aritmatika
            elif re.match(pat_opa, current_token) and num_zone == False and str_zone == False and opr_zone == False and opl_zone == False and opa_zone == False and ident_zone == False:
                temp_opa+=current_token
                current_token = ""
                opa_zone = True

            elif re.match(pat_opa, current_token) and num_zone == False and str_zone == False and opr_zone == False and opl_zone == False and opa_zone == True and ident_zone == False:
                temp_opa+=current_token
                token.append("OP_A:"+temp_opa)
                temp_opa = ""
                current_token = ""
                opa_zone = False

            elif not re.match(pat_opa, current_token) and num_zone == False and str_zone == False and opr_zone == False and opl_zone == False and opa_zone == True and ident_zone == False:
                token.append("OP_A:"+temp_opa)
                temp_opa = ""
                opa_zone = False

                if re.match(r"\"", current_token) and str_zone == False:
                    current_token = ""
                    str_zone = True


            # evaluasi operator logika

            # elif re.match("[!&|]") and num_zone == False and str_zone == False and opr_zone == False and opl_zone == False and opa_zone == False and ident_zone == False:
            #     opl_zone = True





    print(token)
    print(temp_string)
    print(str_zone)





string_this = open("test.txt","r").read() + " "
tokenizing(string_this)
