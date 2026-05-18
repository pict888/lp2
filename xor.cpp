#include <iostream>
#include <string>
using namespace std;

int main() {

    string text;
    int mod;

    // Input text
    cout << "Enter text: ";
    getline(cin, text);

    // Input mod value with validation
    cout << "Enter mod value (<=127): ";
    cin >> mod;

    while(mod > 127) {
        cout << "Invalid! Mod value should not exceed 127.\n";
        cout << "Enter mod value again: ";
        cin >> mod;
    }

    cout << "\nChar\tASCII\tAND\tXOR\n";
    cout << "---------------------------------\n";

    for (int i = 0; i < text.length(); i++) {
        char ch = text[i];

        int ascii = int(ch);
        int andResult = ascii & mod;
        int xorResult = ascii ^ mod;

        cout << ch << "\t"
             << ascii << "\t"
             << andResult << "\t"
             << xorResult << endl;
    }

    return 0;
}

