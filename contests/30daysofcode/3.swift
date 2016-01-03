let response = readLine(stripNewline: true)
let value : Int = Int(response!)!

if(value % 2 == 1) {
	print("Weird")
}
else if(value % 2 == 0 && value >= 2 && value <= 5) {
	print("Not Weird")
}
else if(value % 2 == 0 && value >= 6 && value <= 20) {
	print("Weird")
}
else if(value % 2 == 0 && value > 20) {
	print("Not Weird")
}
