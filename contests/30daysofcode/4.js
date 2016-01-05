function Person(initial_Age) {
    // Add some more code to run some checks on initial_Age
    var age;
    if(initial_Age >= 0) {
        age = initial_Age
    }
    else {
        console.log("This person is not valid, setting age to 0.")
        age = 0
    }

    this.amIOld=function(){
        // Do some computations in here and print out the correct statement to the console
        if(age < 13) {
            console.log("You are young.");
        }
        else if(age >= 13 && age < 18) {
            console.log("You are a teenager.");
        }
        else {
            console.log("You are old.");
        }
    };
    this.yearPasses=function(){
        // Increment the age of the person in here
        age = age + 1;
    };
}
