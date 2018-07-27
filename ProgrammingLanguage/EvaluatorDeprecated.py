#list dari evaluator tidak terpakai


#evaluator operator_aritmetik
#
# elif re.match("(\+|-){2}", current_token) and num_zone == False and str_zone == False and opr_zone == False and opl_zone == False and opa_zone == True and ident_zone == False:
#     token.append("OP_A:"+current_token)
#     current_token = ""
#     opa_zone = False
#
# elif re.match("(\+=|-=|\*=|/=)",current_token) and num_zone == False and str_zone == False and opr_zone == False and opl_zone == False and opa_zone == True and ident_zone == False:
#     token.append("OP_A:"+current_token)
#     current_token = ""
#     opa_zone = False
#
# elif re.match("[\*+-/]", current_token) and num_zone == False and str_zone == False and opr_zone == False and opl_zone == False and opa_zone == True and ident_zone == False:
#     token.append("OP_A:"+current_token)
#     current_token = ""
#     opa_zone = False



#evaluator string1

# elif re.match(r"\"", current_token) and str_zone == False:
#     current_token = ""
#     str_zone = True
#
# elif (re.match(r"\"", current_token) or re.match(r"\\",current_token)) and re.match(r"\\", temp_slash) and str_zone == True:
#     temp_string+="\\"+current_token
#     temp_slash = ""
#     current_token = ""
#
# elif re.match(r"\\", current_token) and str_zone == True:
#     temp_slash+=current_token
#     current_token = ""
#
# elif re.match(r"[^\\\"]", current_token) and str_zone == True:
#     temp_string+=current_token
#     current_token = ""
#
# elif re.match(r"\"", current_token) and str_zone == True:
#     token.append("STRING:"+temp_string)
#     temp_string = ""
#     current_token = ""
#     str_zone = False


#evaluator string0

# elif "\"" in current_token and str_zone == False:
#     current_token = ""
#     str_zone = True
#
#
# elif "\\\"" in current_token and str_zone == True:
#     temp_string += current_token
#     current_token = ""
#
#
# elif "\"" in current_token and str_zone == True:
#     temp_string += current_token[0:-1]
#     current_token = ""
#     token.append("STRING:"+temp_string)
#     temp_string = ""
#     str_zone = False