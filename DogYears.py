human_years = float(input('Enter your human age: '))

#dog age code
dog_years = human_years * 7 
dog_years_int = int(dog_years)
remaining_year_fraction = dog_years - dog_years_int
dog_months = int(remaining_year_fraction * 12)
remaining_month_fraction = (remaining_year_fraction * 12) - dog_months
dog_days = int(remaining_month_fraction * 30)

#cat age code
cat_years = human_years / 9
cat_year_int = int(cat_years)
remaining_cat_year = cat_years - cat_year_int
cat_months = int(remaining_cat_year * 12)
remaining_cat_months = (remaining_cat_year * 12) - cat_months
cat_days = int(remaining_cat_months * 30)

#horse age code
horse_age = 3 * ((human_years**2 - 47) / 7 + 12)
horse_age_int = int(horse_age)
remaining_horse_year = horse_age - horse_age_int
horse_months = int(remaining_horse_year * 12)
remaining_horse_months = (remaining_horse_year * 12) - horse_months
horse_days = int(remaining_horse_months * 30)

print(f'Your dog is {dog_years_int} years {dog_months} months, and {dog_days} day old.', end='')
print(f'Your cat is {cat_year_int} years {cat_months} months, and {cat_days} days old.', end='')
print(f'Your horse is {horse_age_int} years {horse_months} months, and {horse_days} days old.')
