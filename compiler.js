function compile(program, symjs) {const cdx = symjs;const cds = {"+":"+","-":"-",",":",",".":".",">":">","<":"<","[":"[","]":"]","#":"#","^":"^"}
    const symArr = Object.entries(cdx);symArr.forEach(symbol => {program = program.replace(RegExp(symbol[0], "g"), symbol[1])});console.log(program)
    let tape = Array(100).fill(0);let ptr = 0;let isLooping = false;let loopStack = [];let innerLoops = 0;let results = ""
    for(i = 0; i < program.length; i++) {const char = program[i]
    if(isLooping){if(char===cds["["]){innerLoops++};if(char===cds["]"]){if(innerLoops===0){isLooping=false}else{innerLoops--}}continue}
    switch(char){case cds["+"]:tape[ptr]++;break;case cds["-"]:tape[ptr]--;break;
    case cds[","]:tape[ptr]=prompt()[0].charCodeAt();break;case cds["."]:results+=String.fromCharCode(tape[ptr]);break;
    case cds[">"]:ptr++;tape[ptr]=tape[ptr]||0;break;case cds["<"]:ptr--;tape[ptr]=tape[ptr]||0;break;
    case cds["["]:tape[ptr]===0?isLooping=true:loopStack.push(i);break;case cds["]"]:tape[ptr]!==0?i=loopStack[loopStack.length-1]:loopStack.pop();break;
    case cds["#"]:console.log(tape);break;case cds["^"]:console.log((ptr, tape[ptr]));break;
    default:break}}return results.replace(/\n/g,"<br>")}
function printbf(symjs){const input = document.getElementById("input").value;document.getElementById("output").innerHTML = compile(input,symjs)}