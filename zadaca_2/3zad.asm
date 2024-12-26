@24576
D = A;
@5
M = D;

@i
M = 0; 

(loop_s)
@i
D = M;

@5
D = D-A;

@loop_e
D;JEQ
//

@i
A = M;

D = M; 

@vece
D;JLE
//

@5
D = D-M;

@vece
D;JGT

@i
A = M;

D = M;

@5
M = D;

(vece)


//
@i
M = M+1;

@loop_s
0;JMP

(loop_e)

@24576
D = A;
@5
D=D-M;

@kraj
D;JNE

@5
M=0;




(END)
@END
0;JMP