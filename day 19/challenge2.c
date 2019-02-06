
#include <stdio.h>

long long int reg0,reg1,reg2,reg3,reg4;

void printregs(){
	printf("%lld, %lld, %lld, %lld, %lld\n", reg0,reg1,reg2,reg3,reg4);
}

int main(){
	reg0 = 1;
	reg1 = 0;
	reg2 = 0;
	reg3 = 0;
	reg4 = 0;


	lbl0:;
		goto lbl17; //addi 5, 16, 5 (jmp to 16)
	lbl1:;
		reg4 = 1; //seti 1,0,4
	lbl2:;
		reg1 = 1; //seti 1,8,1
	lbl3:;
		reg3 = reg4 * reg1; //mulr 4,1,3
	lbl4:;
		if (reg3 == reg2){ //eqrr 3 2 3
			reg3 = 1;
		}else{
			reg3 = 0;
		}

	lbl5:;
		switch(reg3){
			case 0:
				goto lbl6;
			case 1:
				goto lbl7;
			default:
				goto done;
		}
		//addr 3 5 5

	lbl6:;
		goto lbl8;//addi 5 1 5

	lbl7:;
		reg0 += reg4;//addr 4 0 0
	lbl8:;
		reg1 += 1;//addi 1 1 1

	lbl9:;
		if(reg1 > reg2){//gtrr 1 2 3
			reg3 = 1;
		}else{
			reg3 = 0;
		}
	lbl10:;
		switch(reg3){
			case 0:
				goto lbl11;
			case 1:
				goto lbl12;
			default:
				goto done;
		}
		//addr 5 3 5
	lbl11:;
		goto lbl3;//seti 2 4 5
	lbl12:;
		reg4 += 1;//addi 4 1 4

	lbl13:;
		if(reg4 > reg2){//gtrr 4 2 3
			reg3 = 1;
		}else{
			reg3 = 0;
		}
	lbl14:;
		switch(reg3){
			case 0:
				goto lbl15;
			case 1:
				goto lbl16;
			default:
				goto done;
		}
		// addr 3 5 5
	lbl15:;
		goto lbl2;//seti 1 7 5
	lbl16:;
		goto done;// mulr 5 5 5
	lbl17:;
		reg2 += 2;// addi 2 2 2
	lbl18:;
		reg2 *= 2;// mulr 2 2 2
	lbl19:;
		reg2 *= 19;//mulr 5 2 2
	lbl20:;
		reg2 *= 11;//muli 2 11 2
	lbl21:;
		reg3 += 6;//addi 3 6 3
	lbl22:;
		reg3 = reg3 * 22;//mulr 3 5 3
	lbl23:;
		reg3 += 9;//addi 3 9 3
	lbl24:;
		reg2 += reg3;//addr 2 3 2
	lbl25:;
		switch(reg0){
			case 0:
				goto lbl26;
			case 1:
				goto lbl27;
			default:
				goto done;
		};//addr 5 0 5
	lbl26:;
		goto lbl1;//seti 0 5 5
	lbl27:;
		reg3 = 27;// setr 5 9 3
	lbl28:;
		reg3 = reg3 * 28;// mulr 3 5 3
	lbl29:;
		reg3 = reg3 + 29;// addr 5 3 3
	lbl30:;
		reg3 = reg3 * 30;// mulr 5 3 3
	lbl31:;
		reg3 *= 14;//muli 3 14 3
	lbl32:;
		reg3 = reg3 * 32;//mulr 3 5 3
	lbl33:;
		reg2 += reg3;//addr 2 3 2
	lbl34:;
		reg0 = 0;//seti 0 1 0
	lbl35:;
		goto lbl1;//seti 0 0 5

	done:;

	printf("%d, %d, %d, %d, %d\n", reg0,reg1,reg2,reg3,reg4);
}

//1 
//32 +31
//139 +107
//2920 +2781
//5909 +2989
//9090
//12393
//15710
//21065
//26464
//37632
//44299
//51264
//58455
//66260
//74485
//83096
//92021
//100976
//110329
//120238
//130273
//