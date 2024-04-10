def factorial(n)
  if n == 0 || n == 1
    return 1
  else
    return n * factorial(n - 1)
  end
end

puts "Factorial of 5 is: #{factorial(5)}"
puts "Factorial of 0 is: #{factorial(0)}"
puts "Factorial of 1 is: #{factorial(1)}"
