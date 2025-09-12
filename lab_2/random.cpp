#include <fstream>
#include <iostream>
#include <random>
#include <string>

/**
* Generates a random binary sequence of 128 bit
* 
* @return Generated binary sequence as a string
*/
std::string generate_seq() {
	std::random_device rd;
	std::mt19937 gen(rd());
	std::uniform_int_distribution number(0, 1);

	std::string sequence;

	for (size_t i = 0; i < 128; ++i) {
		sequence += std::to_string(number(gen));
	}

	return sequence;
}

/**
* Saves a sequence to the specified file
* 
* @param filename Path to the file to save
* @param sequence Sequence to save
*/
void save_seq(const std::string& filename, const std::string& sequence) {
	try {
		std::ofstream out;
		out.open(filename);

		if (!out.is_open()) {
			throw std::runtime_error("Failed to open file " + filename);
		}

		out << sequence << std::endl;
		out.close();
	}
	catch (const std::exception& e) {
		std::cerr << e.what() << std::endl;
	}
}

int main() {
	std::string sequence = generate_seq();
	save_seq("sequence_cpp.txt", sequence);

	return 0;
}
