#include <iostream>
using namespace std;

// ---------- Rail Fence Encrypt ----------
string railEncrypt(string text, int key) {

    string rail[10];

    int row = 0;
    bool down = true;

    for(char ch : text) {
        rail[row] += ch;
        if(row == 0)
            down = true;
        else if(row == key - 1)
            down = false;
        if(down)
            row++;
        else
            row--;
    }
    string result = "";
    for(int i = 0; i < key; i++)
        result += rail[i];
    return result;
}

// ---------- Rail Fence Decrypt ----------
string railDecrypt(string cipher, int key) {

    int len = cipher.length();
    string result(len, ' ');
    int row = 0;
    bool down = true;
    int index = 0;
    // Put characters back
    for(int i = 0; i < key; i++) {
        row = 0;
        down = true;
        for(int j = 0; j < len; j++) {
            if(row == i)
                result[j] = cipher[index++];
            if(row == 0)
                down = true;
            else if(row == key - 1)
                down = false;
            if(down)
                row++;
            else
                row--;
        }
    }
    return result;
}

// ---------- Columnar Encrypt ----------
string columnEncrypt(string text, int key) {
    string result = "";
    for(int i = 0; i < key; i++) {
        for(int j = i; j < text.length(); j += key) {
            result += text[j];
        }
    }
    return result;
}

// ---------- Columnar Decrypt ----------
string columnDecrypt(string cipher, int key) {
    string result(cipher.length(), ' ');
    int index = 0;
    for(int i = 0; i < key; i++) {
        for(int j = i; j < cipher.length(); j += key) {
            result[j] = cipher[index++];
        }
    }
    return result;
}

// ---------- Main ----------
int main() {
    string text;
    int key;
    cout << "Enter text: ";
    cin >> text;
    cout << "Enter key: ";
    cin >> key;
    // Rail Fence
    string railCipher = railEncrypt(text, key);
    cout << "\nRail Fence Encrypted: "
         << railCipher;
    cout << "\nRail Fence Decrypted: "
         << railDecrypt(railCipher, key);
    // Columnar
    string columnCipher = columnEncrypt(text, key);
    cout << "\n\nColumnar Encrypted: "
         << columnCipher;
    cout << "\nColumnar Decrypted: "
         << columnDecrypt(columnCipher, key);
    return 0;
}
