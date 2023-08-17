local lives = 10
math.randomseed(os.time())
local randomNumber = math.random(1 , 100)

if lives > 10 then
    print("How did you even get here?! You are only supposed to have 10 lives.")
    print("Good job on breaking the system though, continue playing!")
end

print("Welcome to the higher or lower game!")


while lives > 0 do

    print("You have "..lives.." lives left, guess a number between 1 and 100!")

    number = io.read()

    local number = tonumber(number)

    if number == randomNumber then
        print("You guessed the number! Congratulations!")

        break
    elseif number < 0 then
        print("You may only guess a number between 1 and 100! You guessed a number below 0.")
    elseif number == 69 then
        print("nice")
    elseif number > 100 then
        print("You may only guess a number between 1 and 100! You guessed a number above 100.")
    elseif number < randomNumber then
        print("Incorrect,guess a larger number!")
    elseif number > randomNumber then
        print("Incorrect, guess a smaller number!")  
    end

    lives = lives - 1

    if lives <= 0 then

        print("You failed! How the fuck do you even fail this game??")
        break
    end

end