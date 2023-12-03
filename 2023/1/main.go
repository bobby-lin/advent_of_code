package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	readFile, err := os.Open("2023/1/day1_input.txt")

	if err != nil {
		fmt.Println(err)
	}

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	total := 0

	for fileScanner.Scan() {
		line := fileScanner.Text()
		firstNum := -1
		secondNum := -1
		for i := 0; i < len(line); i++ {
			if line[i] >= 48 && line[i] <= 57 {
				if firstNum == -1 {
					firstNum = int(line[i])
					secondNum = int(line[i])
				} else {
					secondNum = int(line[i])
				}
			}
		}

		calibrationVal := string(firstNum) + string(secondNum)
		calibrationDigits, err := strconv.Atoi(calibrationVal)

		if err != nil {
			fmt.Println(err)
		}

		total += calibrationDigits
	}

	fmt.Println(total)

	readFile.Close()
}
