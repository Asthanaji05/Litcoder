def people_know_secret(n, delay, forget):
    # Array to keep track of the number of people who know the secret on each day
    people = [0] * (n + 1)
    people[1] = 1  # On day 1, one person knows the secret

    for day in range(1, n + 1):
        if people[day] > 0:
            # Spread the secret to new people starting from 'day + delay' to 'day + forget - 1'
            for spread_day in range(day + delay, min(day + forget, n + 1)):
                people[spread_day] += people[day]

    # Sum up the number of people who still remember the secret at the end of day n
    total_people = sum(people[max(1, n - forget + 1):n + 1])
    return total_people

# Input parsing
n = int(input())  # Number of days
delay = int(input())  # Delay days
forget = int(input())  # Forgetting days

# Get the result
result = people_know_secret(n, delay, forget)

# Output the result
print(result)
