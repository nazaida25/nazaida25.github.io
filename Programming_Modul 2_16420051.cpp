#include <bits/stdc++.h>

using namespace std;

double tambah(double n1, double n2){
	//fungsi penjumlahan
	return n1 + n2;
}

double kurang(double n1, double n2){
	//fungsi pengurangan
	return n1 - n2;
}

double kali(double n1, double n2){
	//fungsi perkalian
	return n1 * n2;
}

double bagi(double n1, double n2){
	//fungsi pembagian
	return n1 / n2;
}

double pangkat(double n1, double n2){
	//fungsi perpangkatan
	return pow(n1, n2);
}

double integral(double a, double b){
	//fungsi integral f(x) = x
	return a * a - 2 * a * b + b * b;
}

int main(){
	char oper;
	double num1, num2, hasil = 0;
	bool repeat;
	do{
		system("cls");
        cout << "===========================================================" <<endl;
        cout << "                       Kalkulator Sederhana                " <<endl;
        cout << "-----------------------------------------------------------" <<endl;
        cout << "                       Rumus Operator                      " <<endl;
        cout << "       Penjumlahan  : +             Pengurangan: -         " <<endl;
        cout << "       Perkalian    : *             Pembagian  : :         " <<endl;
        cout << "       Perpangkatan : ^             Integral   : i         " <<endl;
        cout << "===========================================================" <<endl;
        cout << endl ;
        cout << "Masukkan Operator :";
		scanf(" %c", &oper);
		while(!(oper == '+' || oper == '-' || oper == '*' || oper == ':' || oper == '^' || oper == 'i' || oper == 'I')){
			system("cls");
            cout << "===========================================================" <<endl;
            cout << "     Input Tidak Valid! Masukkan Operator yang Sesuai      " <<endl;
            cout << "-----------------------------------------------------------" <<endl;
            cout << "                       Rumus Operator                      " <<endl;
            cout << "       Penjumlahan  : +             Pengurangan: -         " <<endl;
            cout << "       Perkalian    : *             Pembagian  : :         " <<endl;
            cout << "       Perpangkatan : ^             Integral   : i         " <<endl;
            cout << "===========================================================" <<endl;
            cout << endl ;
            cout << " Masukkan Operator : ";
			scanf(" %c", &oper);
		}
		cout << "Masukkan Angka Pertama : ";
		cin >> num1;
		cout << "Masukkan Angka Kedua   : ";
		cin >> num2;
		if(oper == '+'){
			hasil = tambah(num1, num2);
		}else if(oper == '-'){
			hasil = kurang(num1, num2);
		}else if(oper == '*'){
			hasil = kali(num1, num2);
		}else if(oper == ':'){
			hasil = bagi(num1, num2);
		}else if(oper == '^'){
			hasil = pangkat(num1, num2);
		}else{
			hasil = integral(num1, num2);
		}
		cout << "Hasil = " << hasil << "\n";
		char temp;
		cout << "Ulangi? (Y/N) > ";
		scanf(" %c", &temp);
		while(!(temp == 'n' || temp == 'N' || temp == 'y' || temp == 'Y')){
            cout << "===========================================================" <<endl;
            cout << "                       Kalkulator Sederhana                " <<endl;
            cout << "===========================================================" <<endl;
			cout << "Input Tidak Valid! Ulangi? (Y/N) : ";
			scanf(" %c", &temp);
			system("cls");
		}
		if(temp == 'y' || temp == 'Y')
			repeat = 1;
		else
			repeat = 0;
	}while(repeat);
	return 0;
}
