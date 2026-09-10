void ejemplo() {
    // Variable en el STACK (gestión automática)
    int numeroEstatico = 10; 

    // Variable en el HEAP (memoria dinámica pedida manualmente)
    int* numeroDinamico = new int(20); 

    std::cout << "Stack: " << numeroEstatico << std::endl;
    std::cout << "Heap: " << *numeroDinamico << std::endl;

    // Liberación manual del espacio en el HEAP para evitar fugas de memoria
    delete numeroDinamico; 
    numeroDinamico = nullptr;
}

int main() {
    ejemplo();
    return 0;
}