from jamo import h2j

def hangul_to_jamo():
    # Prompt the user for Hangul input
    hangul_text = input("Enter Hangul text: ")
    
    # Convert Hangul to Jamo
    jamo_text = h2j(hangul_text)
    
    # Print the Jamo output
    print(f"Converted Jamo: {jamo_text}")
    
    # Export to a text file
    with open("jamo_output.txt", "w", encoding="utf-8") as file:
        file.write(jamo_text)
    
    print("Jamo output has been exported to jamo_output.txt")

if __name__ == "__main__":
    hangul_to_jamo()
