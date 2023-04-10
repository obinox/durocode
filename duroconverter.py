# cs = '++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.'
cs = '+>>++++[<++++>-]<[<++++++>-]+[<[>>>>+<<<<-]>>>>[<<<<+>>>>>>+<<-]<++++[>++++++++<-]>.[-]<+++[>+++<-]>+[>>.+<<-]>>[-]<<<++[<+++++>-]<.<<[>>>>+<<<<-]>>>>[<<<<+>>>>>>+<<-]<<[>>>>.+<<<++++++++++[<[>>+<<-]>>[<<+>>>>>+++++++++++<<<-]<[>+<-]>[<+>>>>+<<<-]>>>[>>>>>>>>>>>>+>+<<<<<<<<<<<<<-]>>>>>>>>>>>>[-[>>>>+<<<<-]>[>>>>+<<<<-]>>>]>>>[<<<+>>>-]<<<[>>+>+<<<-]>[->[<<<<+>>>>-]<[<<<<+>>>>-]<<<<]<+++++++++[>+++++<-]>>[<<+>>-]<<[>---<-]>.[-]<<<<<<<<<<<<<<<<<-]++++++++++.[-]<-]>>>>[-]<[-]++++++++[>++++++++<-]>--.[-]<,----------[<+>-]>>>>>>+<<<<<<<[>+>>>>>+>[-]<<<<<<<-]>++++++++++>>>>>[[-]<<,<<<<<<<->>>>>>>[<<<<+>>>>-]<<<<[>>>>+>+<<<<<-]>>>>>----------[<<<<<<<<+<[>>>>+<<<<-]>>>>[<<<<+>>>>>>+<<-]>[>-<-]>++++++++++[>+++++++++++<-]<<<<<<[>>>>+<<<<-]>>>>[<<<<+>>>>>>+<<-]>>>>[<<->>-]<<++++++++++[>+<-]>[>>>>>>>>>>>>+>+<<<<<<<<<<<<<-]>>>>>>>>>>>>[-[>>>>+<<<<-]>[>>>>+<<<<-]>>>]>>>[<<<+>>>-]+<<<[>>>-<<<-]>[->[<<<<+>>>>-]<[<<<<+>>>>-]<<<<]<<<<<<<<<<<,[-]]>]>[-+++++++++++[>+++++++++++>+++++++++++<<-]>[-[>>>+<<<-]>>>[<<<+>>>>>>>+>+<<<<<-]>>>>[-[>>>>+<<<<-]>[>>>>+<<<<-]>>>]>>>[<<<+>>>-]<<<[>>+>+<<<-]>[->[<<<<+>>>>-]<[<<<<+>>>>-]<<<<]<<<<<<<<[>>>+<<<-]>>>[<<<+>>>>>>>+>+<<<<<-]<<[>>+<<-]>>[<<+>>>>>>+>+<<<<<-]>>>>[-[>>>>+<<<<-]>[>>>>+<<<<-]>[>>>>+<<<<-]>>]>>>[-]<[>+<-]<[-[<<<<+>>>>-]<<<<]<<<<<<<<]<<<<<<<<<<++++++++++[>++++++++++[<[>>+<<-]>>[<<+>>>>>+++++++++++<<<-]<[>+<-]>[<+>>>>+<<<-]>>>[<<<+>>>-]<<<[>>>+>>>>>+<<<<<<<<-]>>>>>>>>>[>>+<<-]>>[<<+<+>>>-]<<<------------[>>>+<<<-]>>>[<<<+>>>>>>>+>+<<<<<-]>>>>[-[>>>>+<<<<-]>[>>>>+<<<<-]>>>]>>>[<<<+>>>-]<<<[>>+>+<<<-]>>>>>>>[<<<+>>>-]<<<[>>>+<<<<<+>>-]>>>>>>>[<<<+>>>-]<<<[>>>+<<<<<<<<<+>>>>>>-]<<<<<<<[->[<<<<+>>>>-]<[<<<<+>>>>-]<<<<]>[<<<<<<<+>>>>>>>-]<<<<<<<<<+++++++++++[>>>+<<<-]>>>[<<<+>>>>>>>+>+<<<<<-]>>>>[-[>>>>+<<<<-]>[>>>>+<<<<-]>>>]>>>[<<<+>>>-]<<<[>>+>+<<<-]>>>>>>>[<<<+>>>-]<<<[>>>+<<<<<+>>-]>>>>>>>[<<<+>>>-]<<<[>>>+<<<<<<<<<+>>>>>>-]<<<<<<<[->[<<<<+>>>>-]<[<<<<+>>>>-]<<<<]>[<<<<<<<+>>>>>>>-]<<<<<<<<<+++++++++++[>>>>>>>+>+<<<<<<<<-]>>>>>>>[-[>>>>+<<<<-]>[>>>>+<<<<-]>>>]>>>[<<<+>>>-]<<<[>>+>+<<<-]>>>>>>>[<<<+>>>-]<<<[>>>+<<<<<+>>-]>>>>>>>[<<<+>>>-]<<<[>>>+<<<<<<<<<+>>>>>>-]<<<<<<<[->[<<<<+>>>>-]<[<<<<+>>>>-]<<<<]>[<<<<<<<+>>>>>>>-]<<<<<<<----[>>>>>>>+<<<<<<<+[>>>>>>>-<<<<<<<[-]]<<<<<<<[>>>>>>>>>>>>+>+<<<<<<<<<<<<<-][lft@df.lth.se]>>>>>>>>>>>>[-[>>>>+<<<<-]>[>>>>+<<<<-]>[>>>>+<<<<-]>>]>>>[-]<[>+<-]<[-[<<<<+>>>>-]<<<<]<<<<<<[-]]<<<<<<<[-]<<<<-]<-]>>>>>>>>>>>[-]<<]<<<<<<<<<<]'
with open('durolife.txt', 'w', encoding='utf-16') as d:
    sym = {
    "따이":"[<.>-]",
    "딱따라딱":"[>.<-]",
    "여러분":"[<",
    "ㄱㄷ":">-]<",
    "77ㅓ억":"[>",
    "ㅇㅈㅅ": "<-]>",
    "ㅇㅅㅇ": ".",
    "지대루":">",
    "어구래":"<",
    "아":"+",
    "안해":"-",
    "못참지":"[",
    "아이좋아":"]",
    }
    for i,j in sym.items():
        cs = cs.replace(j,i)
    d.write(cs)