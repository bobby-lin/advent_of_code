package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func convertStringDigitToInt(s string, overlapMapping map[string]string, numberMapping map[string]string) string {

	newStr := s

	for key, value := range overlapMapping {
		newStr = strings.ReplaceAll(newStr, key, value)
	}

	for key, value := range numberMapping {
		newStr = strings.ReplaceAll(newStr, key, value)
	}

	return newStr
}

func main() {
	overlapMapping := map[string]string{
		"oneight":   "18",
		"twone":     "21",
		"threeight": "38",
		"fiveight":  "58",
		"eightwo":   "82",
		"eighthree": "83",
	}

	numberMapping := map[string]string{
		"one":   "1",
		"two":   "2",
		"three": "3",
		"four":  "4",
		"five":  "5",
		"six":   "6",
		"seven": "7",
		"eight": "8",
		"nine":  "9",
	}

	readFile, err := os.Open("2023/1/day1_input.txt")

	if err != nil {
		fmt.Println(err)
	}

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	total := 0

	for fileScanner.Scan() {
		line := fileScanner.Text()
		line = convertStringDigitToInt(line, overlapMapping, numberMapping)

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
