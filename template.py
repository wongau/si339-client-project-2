import csv
with open("37th_Early_Bird_Open_Mens_5000_Meters_HS_Open_5K_24.csv", newline='', encoding='utf-8') as file:
   reader = csv.reader(file)
   data = list(reader)

   num_rows = len(data)
   num_cols = len(data[0])

   print(f"Number of rows: {num_rows}")
   print(f"Number of columns: {num_cols}")

meet_name = data[0]  # Column A - h1 (Meet Name)

meet_date = data[1]  # Column B - h2 (Meet Date)
team_results_link = data[2]  # Column C - hyperlink for the team-results section
race_comments = data[3]  # Column E - race-comments section

team_placements = data[6:24]
first_place_team = team_placements[1]
second_place_team = team_placements[2]
third_place_team = team_placements[3]
combined_race_comments = ",".join(race_comments)

top5 = data[27:32]
first = top5[0]
second = top5[1]
third = top5[2]
fourth = top5[3]
fifth = top5[4]

# print(f"First Place: {first}")
# print(f"Second Place: {second}")
# print(f"Third Place: {third}")
# print(f"Fourth Place: {fourth}")
# print(f"Fifth Place: {fifth}")

# print(f"meet name {meet_name}")
# print(f"meet_date {meet_date}")
# print(f"team_results_link {team_results_link}")
# print(f"race_comments{race_comments}")


# Start building the HTML structure
html_content = f'''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{meet_name}</title>
    <link rel="stylesheet" href="styles.css">  
</head>
<body>
    <header>
        <h1>{meet_name}</h1>
        <p>{meet_date}</p>
    </header>

    <div class="container">
        <section class="summary">
            <h2>Meet Summary</h2>
            <p>{combined_race_comments}</p>
        </section>

        <section class="gallery">
            <h2>Photo Gallery</h2>
            <div>
                <img src="IMG_8973.jpg" alt="Male Athletes running the race">
                <img src="IMG_9039.jpg" alt="Female Athletes running the race">
            </div>
        </section>

        <section class="filters">
            <div>
                <label for="gradeFilter">Filter by Grade:</label>
                <select id="gradeFilter">
                    <option value="all">All Grades</option>
                    <option value="9">9th Grade</option>
                    <option value="10">10th Grade</option>
                    <option value="11">11th Grade</option>
                    <option value="12">12th Grade</option>
                </select>
            </div>
            <div>
                <label for="genderFilter">Filter by Gender:</label>
                <select id="genderFilter">
                    <option value="all">All Genders</option>
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                </select>
            </div>
        </section>

        <section class="results">
            <h2>Team Placements</h2>
            <table class="accessible">
                <thead>
                    <tr>
                        <th>Team</th>
                        <th>Score</th>
                        <th>Placement</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>{first_place_team[1]}</td>
                        <td>{first_place_team[2]}</td>
                        <td>{first_place_team[0]}</td>
                    </tr>
                    <tr>
                        <td>{second_place_team[1]}</td>
                        <td>{second_place_team[2]}</td>
                        <td>{second_place_team[0]}</td>
                    </tr>
                    <tr>
                        <td>{third_place_team[1]}</td>
                        <td>{third_place_team[2]}</td>
                        <td>{third_place_team[0]}</td>
                    </tr>
                </tbody>
            </table>
        </section>

        <section class="individual-results">
            <h2>Individual Placements</h2>
            <table class="accessible">
                <thead>
                    <tr>
                        <th>Place</th>
                        <th>Grade</th>
                        <th>Name</th>
                        <th>Time</th>
                        <th>Team</th>
                        <th>Profile Pic</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>{first[0]}</td>
                        <td>{first[1]}</td>
                        <td><a href="{first[3]}">{first[2]}</a></td>
                        <td>{first[4]}</td>
                        <td><a href="{first[6]}">{first[5]}</a></td>
                        <td><img class="profile-pic" src="{first[7]}" alt="Profile picture of {first[2]}"></td>
                    </tr>
                    <tr>
                        <td>{second[0]}</td>
                        <td>{second[1]}</td>
                        <td><a href="{second[3]}">{second[2]}</a></td>
                        <td>{second[4]}</td>
                        <td><a href="{second[6]}">{second[5]}</a></td>
                        <td><img class="profile-pic" src="{second[7]}" alt="Profile picture of {second[2]}"></td>
                    </tr>
                    <tr>
                        <td>{third[0]}</td>
                        <td>{third[1]}</td>
                        <td><a href="{third[3]}">{third[2]}</a></td>
                        <td>{third[4]}</td>
                        <td><a href="{third[6]}">{third[5]}</a></td>
                        <td><img class="profile-pic" src="{third[7]}" alt="Profile picture of {third[2]}"></td>
                    </tr>
                    <tr>
                        <td>{fourth[0]}</td>
                        <td>{fourth[1]}</td>
                        <td><a href="{fourth[3]}">{fourth[2]}</a></td>
                        <td>{fourth[4]}</td>
                        <td><a href="{fourth[6]}">{fourth[5]}</a></td>
                        <td><img class="profile-pic" src="{fourth[7]}" alt="Profile picture of {fourth[2]}"></td>
                    </tr>
                    <tr>
                        <td>{fifth[0]}</td>
                        <td>{fifth[1]}</td>
                        <td><a href="{fifth[3]}">{fifth[2]}</a></td>
                        <td>{fifth[4]}</td>
                        <td><a href="{fifth[6]}">{fifth[5]}</a></td>
                        <td><img class="profile-pic" src="{fifth[7]}" alt="Profile picture of {fifth[2]}"></td>
                    </tr>
                    <!-- Additional athletes would follow here -->
                </tbody>
            </table>
        </section>
    </div>
</body>

</html>'''

print(html_content)