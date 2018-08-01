import re

pat_alp = re.compile(r"[A-Za-z]")
pat_al_ident_start = re.compile(r"[A-Za-z_]")
pat_opa = re.compile(r"[-\+\*/%]")
pat_opl = re.compile(r"[!\|&]")
pat_opr = re.compile(r"[<=>]")
pat_angka = re.compile(r"[0-9]") # angka
pat_allowed_ident = re.compile(r"[A-Za-z0-9_]")
pat_punc = re.compile(r"[\{\}\(\)\[\]]")
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

        for j in range(1):

            # evaluasi identifier dan keyword
            if re.match(r"\s",current_token) and str_zone == False:
                current_token = ""
                if num_zone == True and temp_num != "":
                    token.append("NUM:" + temp_num)
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

                if opl_zone == True and temp_opl != "":
                    if re.match(r"!", temp_opl):
                        token.append("OP_L:"+temp_opl)
                    else:
                        token.append("UNK_SYM:"+temp_opl)
                    temp_opl = ""
                    opl_zone = False

                if opr_zone == True and temp_opr != "":
                    if re.match(r"(<|>)", temp_opr):
                        token.append("OP_R:"+temp_opr)
                    else:
                        token.append("UNK_SYM:"+temp_opr)
                    temp_opr = ""
                    opr_zone = False

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

                # valuasi operator aritmatik
                if re.match(r"[\*\+-/]", current_token):
                    temp_opa+=current_token
                    current_token = ""
                    opa_zone = True

                #evaluasi operator logika
                if re.match(pat_opl, current_token):
                    temp_opl += current_token
                    current_token = ""
                    opl_zone = True

                #evaluasi operator relasi
                if re.match(pat_opr,current_token):
                    temp_opr += current_token
                    current_token = ""
                    opr_zone = True

                if re.match(pat_punc, current_token):
                    token.append("PUNC:" + current_token)
                    current_token = ""

            # evaluasi angka
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
                if re.match(pat_al_ident_start,current_token):
                    temp_ident+=current_token
                    ident_zone = True
                    current_token = ""

                # evaluator operator logika
                if re.match(pat_opl, current_token):
                    temp_opl+=current_token
                    opl_zone = True
                    current_token = ""

                if re.match(pat_punc, current_token):
                    token.append("PUNC:" + current_token)
                    current_token = ""

                if re.match(pat_opr, current_token):
                    temp_opr += current_token
                    current_token = ""
                    opr_zone = True

                if (not (re.match(pat_allowed_ident, current_token) or re.match(pat_opa, current_token) or re.match(pat_opl, current_token) or re.match(pat_opr, current_token) or re.match(pat_punc,current_token))) and current_token != " " and current_token != "":
                    token.append("UNK_SYM:" + current_token)
                    current_token = ""

            #evaluator string
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

            #evaluasi operator aritmatika
            elif re.match(pat_opa, current_token) and num_zone == False and str_zone == False and opr_zone == False and opl_zone == False and opa_zone == False and ident_zone == False:
                temp_opa+=current_token
                current_token = ""
                opa_zone = True

            elif re.match(r"[=\+\-\*]", current_token) and num_zone == False and str_zone == False and opr_zone == False and opl_zone == False and opa_zone == True and ident_zone == False:
                temp_opa+=current_token
                if re.match(r"(\+\+|--|\+=|-=|\*=|/=|-\+|\+-|\*-|/-)",temp_opa):
                    token.append("OP_A:"+temp_opa)
                else:
                    token.append("UNK_SYM:"+temp_opa)
                temp_opa = ""
                current_token = ""
                opa_zone = False

            elif not re.match(pat_opa, current_token) and num_zone == False and str_zone == False and opr_zone == False and opl_zone == False and opa_zone == True and ident_zone == False:
                token.append("OP_A:"+temp_opa)
                temp_opa = ""
                opa_zone = False

                if re.match(r"\"", current_token):
                    current_token = ""
                    str_zone = True

                if re.match(pat_al_ident_start,current_token):
                    temp_ident+=current_token
                    ident_zone = True
                    current_token = ""

                if re.match(pat_angka,current_token):
                    temp_num += current_token
                    current_token = ""
                    num_zone = True

                if re.match(pat_punc, current_token):
                    token.append("PUNC:" + current_token)
                    current_token = ""

                if re.match(pat_opl, current_token):
                    temp_opl += current_token
                    current_token = ""
                    opl_zone = True

                if re.match(pat_opr,current_token):
                    temp_opr += current_token
                    current_token = ""
                    opr_zone = True

                if (not (re.match(pat_allowed_ident, current_token) or re.match(pat_opa, current_token) or re.match(pat_opl, current_token) or re.match(pat_opr, current_token) or re.match(pat_punc,current_token))) and current_token != " " and current_token != "":
                    token.append("UNK_SYM:" + current_token)
                    current_token = ""

            # evaluator operator logika
            elif re.match(pat_opl, current_token) and num_zone == False and str_zone == False and opr_zone == False and opl_zone == False and opa_zone == False and ident_zone == False:
                temp_opl+=current_token
                current_token = ""
                opl_zone = True

            elif re.match(pat_opl, current_token) and num_zone == False and str_zone == False and opr_zone == False and opl_zone == True and opa_zone == False and ident_zone == False:

                if re.match(r"!", temp_opl) and re.match(r"!", current_token):
                    token.append("OP_L:"+temp_opl)
                    temp_opl = ""
                    temp_opl+="!"
                    current_token = ""

                else:
                    temp_opl+=current_token
                    if re.match("(\|\||&&)", temp_opl):
                        token.append("OP_L:"+temp_opl)
                        temp_opl = ""
                        current_token = ""
                        opl_zone = False
                    else:
                        token.append("UNK_SYM:"+temp_opl)
                        temp_opl = ""
                        current_token = ""
                        opl_zone = False

            elif not re.match(pat_opl, current_token) and num_zone == False and str_zone == False and opr_zone == False and opl_zone == True and opa_zone == False and ident_zone == False:

                if re.match(r"!", temp_opl) and re.match(r"=", current_token):
                    temp_opr += temp_opl + current_token
                    token.append("OP_R:"+temp_opr)
                    temp_opl = ""
                    temp_opr = ""
                    opl_zone = False

                elif re.match(r"!", temp_opl):
                    token.append("OP_L:"+temp_opl)
                    temp_opl = ""
                    opl_zone = False

                else:
                    token.append("UNK_SYM:"+temp_opl)
                    temp_opl = ""
                    opl_zone = False

                if re.match(r"\"", current_token):
                    current_token = ""
                    str_zone = True

                if re.match(pat_angka,current_token):
                    temp_num += current_token
                    num_zone = True

                if re.match(pat_al_ident_start,current_token):
                    temp_ident+=current_token
                    ident_zone = True
                    current_token = ""

                if re.match(pat_opa,current_token):
                    temp_opa += current_token
                    opa_zone = True

                if re.match(pat_punc, current_token):
                    token.append("PUNC:" + current_token)

                current_token = ""
            # evaluator operator relasi

            elif re.match(pat_opr, current_token) and num_zone == False and str_zone == False and opr_zone == False and opl_zone == False and opa_zone == False and ident_zone == False:
                temp_opr+=current_token
                current_token = ""
                opr_zone = True

            elif re.match(pat_opr, current_token) and num_zone == False and str_zone == False and opr_zone == True and opl_zone == False and opa_zone == False and ident_zone == False:

                if (re.match(r"<", temp_opr) and re.match(r"<", current_token)) or (re.match(r">", temp_opr) and re.match(r">", current_token)):
                    token.append("OP_R"+current_token)
                    temp_opr = ""
                    temp_opr+=current_token
                    current_token = ""

                else:
                    temp_opr+=current_token
                    if re.match(r"(<=|==|>=)", temp_opr):
                        token.append("OP_R:"+temp_opr)
                        temp_opr = ""
                        current_token = ""
                        opr_zone = False
                    else:
                        token.append("UNK_SYM:"+temp_opr)
                        temp_opr = ""
                        current_token = ""
                        opr_zone = False



            elif (not re.match(pat_opr, current_token)) and num_zone == False and str_zone == False and opr_zone == True and opl_zone == False and opa_zone == False and ident_zone == False:
                if re.match(r"(<|>)", temp_opr):
                    token.append("OP_R:"+temp_opr)
                    temp_opr = ""
                    opr_zone = False

                else:
                    token.append("UNK_SYM:"+temp_opr)
                    temp_opr = ""
                    opr_zone = False

                if re.match(r"\"", current_token):
                    current_token = ""
                    str_zone = True


                if re.match(pat_angka,current_token):
                    temp_num += current_token
                    current_token = ""
                    num_zone = True

                if re.match(pat_al_ident_start,current_token):
                    temp_ident+=current_token
                    ident_zone = True
                    current_token = ""

                if re.match(pat_opa,current_token):
                    temp_opa += current_token
                    current_token = ""
                    opa_zone = True

                if re.match(pat_punc, current_token):
                    token.append("PUNC:" + current_token)
                    current_token = ""

            #evaluator separator/ punctuator
            elif re.match(pat_punc, current_token) and num_zone == False and str_zone == False and opr_zone == False and opl_zone == False and opa_zone == False and ident_zone == False:
                token.append("PUNC:"+current_token)
                current_token = ""

            # evaluator simbol yang belum di klasifikasi
            elif (not (re.match(pat_allowed_ident, current_token) or re.match(pat_opa, current_token) or re.match(pat_opl,current_token) or re.match(pat_opr, current_token) or re.match(pat_punc,current_token))) and current_token != " " and current_token != "":
                token.append("UNK_SYM:" + current_token)
                current_token = ""

    print(token)

string_this = open("test.txt","r").read() + " "
tokenizing(string_this)
