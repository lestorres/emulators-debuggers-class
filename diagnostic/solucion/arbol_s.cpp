#include <iostream>

int main() {
    const int altura = 8;

    for (int i = 0; i < altura; ++i) {
        // Espacios en blanco para centrar el árbol
        for (int j = 0; j < altura - i - 1; ++j)
            std::cout << " ";

        // Asteriscos del nivel actual
        for (int j = 0; j < 2 * i + 1; ++j)
            std::cout << "*";

        std::cout << std::endl;
    }

    // Tronco del árbol
    for (int i = 0; i < altura - 1; ++i) 
	    //Había cambiar el "10" por un "0"
        std::cout << " ";
    std::cout << "|" << std::endl;
    
    return 0;
}
