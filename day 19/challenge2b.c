


#include <stdio.h>



int main(){
	long long int register reg0 = 0;
	long long int register reg1 = 0;
	long long int register reg4 = 1;


	for(reg4 = 1; reg4 <= 10551377; reg4++){
		if( 10551377 % reg4 == 0){
			reg0 += reg4;
		}

		// for(reg1 = 1; reg1 <= 10551377; reg1++){

		// 	if(reg4*reg1 == 10551377){
		// 		printf(">%lld,%lld, %lld, %lld\n",reg4,reg1,reg4*reg1, 10551377/reg4);
		// 		reg0 += reg4;
		// 		break;
		// 	}

		// }

		if(reg4%100==0){
			printf("%lld, %lld, %lld\n", reg0,reg1,reg4);;
		}
	}

	printf("%lld, %lld, %lld\n", reg0,reg1,reg4);

}



