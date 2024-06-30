import datetime
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText

def send_email(receiver_email,choice):
    sender_email = "------------------"  # Replace with your email address
    sender_password = "-------"  # Replace with your email password
    # Create the email content
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "election voted successfully"
    body = f"Thank you for your vote to {choice}."
    message.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server and send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
def election_voting_system():
    # Initialize vote counters for each candidate
    votes = {"Ram": 0, "Ravi": 0, "Mona": 0, "Siva": 0, "NOTA": 0}
    
    # Predefined list of valid voter IDs
    valid_voter_ids = {"Voter1": "101", "Voter2": "102", "Voter3": "103","voter4" : "104" , "voter5" : "105" , "voter6" : "111"}
    
    # Track voters who have already voted to prevent double voting
    voted_voters = set()
    
    while True:
        # Display voting options
        print("\nElection Voting System")
        print("Press 1 for Ram")
        print("Press 2 for Ravi")
        print("Press 3 for Mona")
        print("Press 4 for Siva")
        print("Press 5 for NOTA")
        print("Press 0 to End Voting and Show Results")
        
        voter_id = input("Enter your voter ID: ")
        
        if voter_id in voted_voters:
            print("You have already voted. Thank you!")
            continue
        
        if voter_id not in valid_voter_ids.values():
            print("Invalid voter ID. Please try again.")
            continue
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 5.")
            continue
        
        if choice == 1:
            votes["Ram"] += 1
            print("You voted for Ram.")
        elif choice == 2:
            votes["Ravi"] += 1
            print("You voted for Ravi.")
        elif choice == 3:
            votes["Mona"] += 1
            print("You voted for Mona.")
        elif choice == 4:
            votes["Siva"] += 1
            print("You voted for Sri.")
        elif choice == 5:
            votes["NOTA"] += 1
            print("You voted for NOTA.")
        elif choice == 0:
            break
        else:
            print("Invalid choice! Please enter a number between 0 and 5.")
            continue
        
        # Mark this voter as having voted
        voted_voters.add(voter_id)
        
        # Send a success message
        print(f"Vote successful for voter ID: {voter_id}. You have voted successfully.")
        print("current date and time")  
        today=datetime.date.today()
        print("current date",today)
        current_time=datetime.datetime.now().time()
        print("current time",current_time)

    # Display the final vote count
    print("\nFinal Vote Count:")
    for candidate, count in votes.items():
        print(f"{candidate}: {count} votes")

# Run the voting system
election_voting_system()