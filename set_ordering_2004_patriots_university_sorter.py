'''
This script sorts the universities of the 2004 New England Patriots roster and print them out in alphabetical order.
demonstrating stdtypes (standard library) set in that it will only print out unique universities since it is a set.
'''

from logging import info, INFO, basicConfig, error
from colorama import Fore, Style
basicConfig(level=INFO, format="%(message)s")

patriots_2004_players = [
    {"full_name": "P. K. Sam", "position": "WR", "pro_bowler": "No", "all_pro": "No", "university": "Florida State University"},
    {"full_name": "J. J. Stokes", "position": "WR", "pro_bowler": "No", "all_pro": "No", "university": "University of California, Los Angeles (UCLA)"},
    {"full_name": "Tom Brady", "position": "QB", "pro_bowler": "No", "all_pro": "No", "university": "University of Michigan"},
    {"full_name": "Rohan Davey", "position": "QB", "pro_bowler": "No", "all_pro": "No", "university": "Louisiana State University (LSU)"},
    {"full_name": "Kliff Kingsbury", "position": "QB", "pro_bowler": "No", "all_pro": "No", "university": "Texas Tech University"},
    {"full_name": "Kurt Kittner", "position": "QB", "pro_bowler": "No", "all_pro": "No", "university": "University of Illinois"},
    {"full_name": "Jim Miller", "position": "QB", "pro_bowler": "No", "all_pro": "No", "university": "Michigan State University"},
    {"full_name": "Mike Cloud", "position": "RB", "pro_bowler": "No", "all_pro": "No", "university": "Boston College"},
    {"full_name": "Corey Dillon", "position": "RB", "pro_bowler": "No", "all_pro": "No", "university": "University of Washington"},
    {"full_name": "Malaefou MacKenzie", "position": "FB", "pro_bowler": "No", "all_pro": "No", "university": "University of Southern California (USC)"},
    {"full_name": "Fred McCrary", "position": "FB", "pro_bowler": "No", "all_pro": "No", "university": "Mississippi State University"},
    {"full_name": "Patrick Pass", "position": "FB", "pro_bowler": "No", "all_pro": "No", "university": "University of Georgia"},
    {"full_name": "Cedric Cobbs", "position": "RB", "pro_bowler": "No", "all_pro": "No", "university": "University of Arkansas"},
    {"full_name": "Kevin Faulk", "position": "RB", "pro_bowler": "No", "all_pro": "No", "university": "Louisiana State University (LSU)"},
    {"full_name": "Rabih Abdullah", "position": "RB", "pro_bowler": "No", "all_pro": "No", "university": "Lehigh University"},
    {"full_name": "Deion Branch", "position": "WR", "pro_bowler": "No", "all_pro": "No", "university": "University of Louisville"},
    {"full_name": "Troy Brown", "position": "WR/PR", "pro_bowler": "No", "all_pro": "No", "university": "Marshall University"},
    {"full_name": "Chas Gessner", "position": "WR", "pro_bowler": "No", "all_pro": "No", "university": "Brown University"},
    {"full_name": "David Givens", "position": "WR", "pro_bowler": "No", "all_pro": "No", "university": "University of Notre Dame"},
    {"full_name": "Michael Jennings", "position": "WR", "pro_bowler": "No", "all_pro": "No", "university": "Florida State University"},
    {"full_name": "Bethel Johnson", "position": "WR/KR", "pro_bowler": "No", "all_pro": "No", "university": "Texas A&M University"},
    {"full_name": "David Patten", "position": "WR", "pro_bowler": "No", "all_pro": "No", "university": "Western Carolina University"},
    {"full_name": "Kevin Kasper", "position": "WR", "pro_bowler": "No", "all_pro": "No", "university": "University of Iowa"},
    {"full_name": "Matt Cercone", "position": "TE", "pro_bowler": "No", "all_pro": "No", "university": "University at Buffalo"},
    {"full_name": "Zeron Flemister", "position": "TE", "pro_bowler": "No", "all_pro": "No", "university": "University of Iowa"},
    {"full_name": "Daniel Graham", "position": "TE", "pro_bowler": "No", "all_pro": "No", "university": "University of Colorado Boulder"},
    {"full_name": "Andy Mignery", "position": "TE", "pro_bowler": "No", "all_pro": "No", "university": "University of Michigan"},
    {"full_name": "Christian Fauria", "position": "TE", "pro_bowler": "No", "all_pro": "No", "university": "University of Colorado Boulder"},
    {"full_name": "Benjamin Watson", "position": "TE", "pro_bowler": "No", "all_pro": "No", "university": "University of Georgia"},
    {"full_name": "Jed Weaver", "position": "TE", "pro_bowler": "No", "all_pro": "No", "university": "University of Oregon"},
    {"full_name": "Joe Andruzzi", "position": "G", "pro_bowler": "No", "all_pro": "No", "university": "Southern Connecticut State University"},
    {"full_name": "Wilbert Brown", "position": "G", "pro_bowler": "No", "all_pro": "No", "university": "University of Houston"},
    {"full_name": "Jack Fadule", "position": "T", "pro_bowler": "No", "all_pro": "No", "university": "Harvard University"},
    {"full_name": "Brandon Gorin", "position": "T", "pro_bowler": "No", "all_pro": "No", "university": "Purdue University"},
    {"full_name": "Bob Hallen", "position": "C", "pro_bowler": "No", "all_pro": "No", "university": "Kent State University"},
    {"full_name": "Russ Hochstein", "position": "G", "pro_bowler": "No", "all_pro": "No", "university": "University of Nebraska–Lincoln"},
    {"full_name": "Adrian Klemm", "position": "T", "pro_bowler": "No", "all_pro": "No", "university": "University of Hawaii at Manoa"},
    {"full_name": "Dan Koppen", "position": "C", "pro_bowler": "No", "all_pro": "No", "university": "Boston College"},
    {"full_name": "Gene Mruczkowski", "position": "G", "pro_bowler": "No", "all_pro": "No", "university": "Purdue University"},
    {"full_name": "Stephen Neal", "position": "G", "pro_bowler": "No", "all_pro": "No", "university": "California State University, Bakersfield"},
    {"full_name": "Tim Provost", "position": "T", "pro_bowler": "No", "all_pro": "No", "university": "San Jose State University"},
    {"full_name": "David Pruce", "position": "T", "pro_bowler": "No", "all_pro": "No", "university": "none"},
    {"full_name": "Jamil Soriano", "position": "G", "pro_bowler": "No", "all_pro": "No", "university": "Harvard University"},
    {"full_name": "James O. Williams", "position": "T", "pro_bowler": "No", "all_pro": "No", "university": "University of Georgia"},
    {"full_name": "Tom Ashworth", "position": "T", "pro_bowler": "No", "all_pro": "No", "university": "University of Colorado Boulder"},
    {"full_name": "Billy Yates", "position": "G", "pro_bowler": "No", "all_pro": "No", "university": "Texas A&M University"},
    {"full_name": "Matt Light", "position": "T", "pro_bowler": "No", "all_pro": "No", "university": "Purdue University"},
    {"full_name": "Rodney Bailey", "position": "DE", "pro_bowler": "No", "all_pro": "No", "university": "Ohio State University"},
    {"full_name": "Dwight Johnson", "position": "DE", "pro_bowler": "No", "all_pro": "No", "university": "Baylor University"},
    {"full_name": "Marquise Hill", "position": "DE", "pro_bowler": "No", "all_pro": "No", "university": "Louisiana State University (LSU)"},
    {"full_name": "Ethan Kelley", "position": "NT", "pro_bowler": "No", "all_pro": "No", "university": "Baylor University"},
    {"full_name": "Dan Klecko", "position": "NT", "pro_bowler": "No", "all_pro": "No", "university": "Temple University"},
    {"full_name": "Buck Rasmussen", "position": "DE", "pro_bowler": "No", "all_pro": "No", "university": "University of Nebraska–Lincoln"},
    {"full_name": "Richard Seymour", "position": "DE", "pro_bowler": "Yes", "all_pro": "Yes", "university": "University of Georgia"},
    {"full_name": "Keith Traylor", "position": "NT", "pro_bowler": "No", "all_pro": "No", "university": "Central State University"},
    {"full_name": "Ty Warren", "position": "DE", "pro_bowler": "No", "all_pro": "No", "university": "Texas A&M University"},
    {"full_name": "Vince Wilfork", "position": "NT", "pro_bowler": "No", "all_pro": "No", "university": "University of Miami"},
    {"full_name": "Jarvis Green", "position": "DE", "pro_bowler": "No", "all_pro": "No", "university": "Louisiana State University (LSU)"},
    {"full_name": "Tully Banta-Cain", "position": "OLB", "pro_bowler": "No", "all_pro": "No", "university": "University of California, Berkeley"},
    {"full_name": "Tedy Bruschi", "position": "ILB", "pro_bowler": "No", "all_pro": "No", "university": "University of Arizona"},
    {"full_name": "Don Davis", "position": "ILB", "pro_bowler": "No", "all_pro": "No", "university": "University of Kansas"},
    {"full_name": "Quinn Dorsey", "position": "OLB", "pro_bowler": "No", "all_pro": "No", "university": "University of Oregon"},
    {"full_name": "Lawrence Flugence", "position": "ILB", "pro_bowler": "No", "all_pro": "No", "university": "Texas Tech University"},
    {"full_name": "Larry Izzo", "position": "ILB", "pro_bowler": "No", "all_pro": "No", "university": "Rice University"},
    {"full_name": "Ted Johnson", "position": "ILB", "pro_bowler": "No", "all_pro": "No", "university": "University of Colorado Boulder"},
    {"full_name": "Justin Kurpeikis", "position": "ILB", "pro_bowler": "No", "all_pro": "No", "university": "Penn State University"},
    {"full_name": "Roman Phifer", "position": "ILB", "pro_bowler": "No", "all_pro": "No", "university": "University of California, Los Angeles (UCLA)"},
    {"full_name": "Grant Steen", "position": "OLB", "pro_bowler": "No", "all_pro": "No", "university": "University of Iowa"},
    {"full_name": "Mike Vrabel", "position": "OLB", "pro_bowler": "No", "all_pro": "No", "university": "Ohio State University"},
    {"full_name": "Rosevelt Colvin", "position": "OLB", "pro_bowler": "No", "all_pro": "No", "university": "Purdue University"},
    {"full_name": "Matt Chatham", "position": "OLB", "pro_bowler": "No", "all_pro": "No", "university": "University of South Dakota"},
    {"full_name": "Willie McGinest", "position": "OLB", "pro_bowler": "Yes", "all_pro": "No", "university": "University of Southern California (USC)"},
    {"full_name": "Terrell Buckley", "position": "CB", "pro_bowler": "No", "all_pro": "No", "university": "Florida State University"},
    {"full_name": "Je'Rod Cherry", "position": "FS", "pro_bowler": "No", "all_pro": "No", "university": "University of California, Berkeley"},
    {"full_name": "Scott Farley", "position": "SS", "pro_bowler": "No", "all_pro": "No", "university": "Williams College"},
    {"full_name": "Randall Gay", "position": "CB", "pro_bowler": "No", "all_pro": "No", "university": "Louisiana State University (LSU)"},
    {"full_name": "Rodney Harrison", "position": "SS", "pro_bowler": "No", "all_pro": "No", "university": "Western Illinois University"},
    {"full_name": "Ty Law", "position": "CB", "pro_bowler": "Yes", "all_pro": "No", "university": "University of Michigan"},
    {"full_name": "Shawn Mayer", "position": "FS", "pro_bowler": "No", "all_pro": "No", "university": "Penn State University"},
    {"full_name": "Christian Morton", "position": "CB", "pro_bowler": "No", "all_pro": "No", "university": "University of Illinois"},
    {"full_name": "Tyrone Poole", "position": "CB", "pro_bowler": "No", "all_pro": "No", "university": "Fort Valley State University"},
    {"full_name": "Dexter Reid", "position": "SS", "pro_bowler": "No", "all_pro": "No", "university": "University of North Carolina at Chapel Hill"},
    {"full_name": "Asante Samuel", "position": "CB", "pro_bowler": "No", "all_pro": "No", "university": "University of Central Florida"},
    {"full_name": "Guss Scott", "position": "FS", "pro_bowler": "No", "all_pro": "No", "university": "University of Florida"},
    {"full_name": "Earthwind Moreland", "position": "CB", "pro_bowler": "No", "all_pro": "No", "university": "Georgia Southern University"},
    {"full_name": "Hank Poteat", "position": "CB", "pro_bowler": "No", "all_pro": "No", "university": "University of Pittsburgh"},
    {"full_name": "Eugene Wilson", "position": "FS", "pro_bowler": "No", "all_pro": "No", "university": "University of Illinois"},
    {"full_name": "Josh Miller", "position": "P", "pro_bowler": "No", "all_pro": "No", "university": "University of Arizona"},
    {"full_name": "Brian Sawyer", "position": "LS", "pro_bowler": "No", "all_pro": "No", "university": "none"},
    {"full_name": "Cody Scates", "position": "P", "pro_bowler": "No", "all_pro": "No", "university": "Texas A&M University"},
    {"full_name": "Adam Vinatieri", "position": "K", "pro_bowler": "No", "all_pro": "No", "university": "South Dakota State University"},
    {"full_name": "Eric Alexander", "position": "ILB", "pro_bowler": "No", "all_pro": "No", "university": "Louisiana State University (LSU)"},
    {"full_name": "Kory Chapman", "position": "RB", "pro_bowler": "No", "all_pro": "No", "university": "Jacksonville State University"},
    {"full_name": "Ricky Bryant", "position": "WR", "pro_bowler": "No", "all_pro": "No", "university": "Hofstra University"},
    {"full_name": "Cedric James", "position": "WR", "pro_bowler": "No", "all_pro": "No", "university": "Texas Christian University (TCU)"},
    {"full_name": "Omare Lowe", "position": "CB", "pro_bowler": "No", "all_pro": "No", "university": "University of Washington"},
    {"full_name": "Lance Nimmo", "position": "T", "pro_bowler": "No", "all_pro": "No", "university": "West Virginia University"}
]

universities = set()
for player in patriots_2004_players:
    # skip if the university is 'none', empty, or null
    if player["university"] in ["none", "", None]:
        continue
    universities.add(player["university"])

for university in sorted(universities):
    info(Fore.GREEN + university + Style.RESET_ALL)