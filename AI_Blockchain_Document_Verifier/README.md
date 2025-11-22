AI-Powered Blockchain Document Verifier

This project is my capstone for the Kaggle 5-Day AI Agents Intensive Course.

Objective :
This project is a simple demo prototype that shows how Artificial Intelligence and Blockchain can work together to verify documents. The idea behind this project is that, in the real world, important files such as certificates, offers, agreements, or government documents should have a trusted way to confirm their originality. Instead of manually checking them, AI can analyze the file and Blockchain can store its fingerprint (hash) in a tamper-proof way.

Aim :
My aim here is not to build a full production system, but to create a small working model that demonstrates the core concept. In the future, the same approach can be extended with more advanced AI checks, better smart contracts, and automated verification pipelines.

⸻

What This Project Does;

	•	You upload any document.
	•	The AI agent checks if the document is valid, clear, or tampered.
	•	(Optional) The document is hashed using a blockchain smart contract.
	•	Finally, you get a short verification report.

The goal was to connect AI + Blockchain in a basic and understandable way.

⸻

Why I Built This

I’m a blockchain technology student, so I wanted to explore how AI agents can work together with blockchain. This project helped me understand how agents take actions, use tools, and interact with external systems.

⸻

How This Demo Works (Simple Explanation)

The project has two main parts:

1. Python (AI Side) – Generates the Document Hash

You run one Python file:  "run_demo.py"

This script automatically finds your PDF file, generates its SHA-256 hash.
This hash represents the unique fingerprint of your document.

2. Solidity Smart Contract (Blockchain Side)

A simple smart contract named: "DocumentVerifier.sol"

The contract allows you to:
	•	registerHash(hash) → store the hash on blockchain
	•	verifyDocument(hash) → check if a document hash already exists

When you paste the hash into Remix and submit it to the contract, you will get:
	•	true → the document is registered
	•	false → the document is not registered / modified

This demonstrates how blockchain ensures immutability and tamper detection.


⸻


Steps for the Execution of project:

This project includes a Python script named run_demo.py.
This file is the starting point of the entire AI + Blockchain verification process.

Below is a clear explanation of what it does and what the AI does

⸻

1. What Happens When You Run run_demo.py?

When you run: "run_demo.py"

The script automatically performs these tasks:

Step 1 → Auto-detect your PDF
	•	The script looks inside the project folder.
	•	It finds the first PDF file (example: sample_document.pdf).
	•	You do NOT need to type any file name.
   ~ Just run the code.

Step 2 → Generate SHA-256 Hash
	•	It reads the file.
	•	Converts the file into a unique SHA-256 hash.
	•	This hash acts like a fingerprint of the document.

Example hash:  "0xab34f8c92…something"

Step 3 → Display the Hash on Screen
You simply copy the hash and paste it into Remix during the blockchain step.


 2. What AI Does in This Demo?

This is a demo prototype, so the AI part is simple but functional.

Inside the script, the AI performs:

AI Role → “Smart Checking” the Document Before Blockchain

The AI model is used to:

✓ Read the document (PDF)
✓ Understand its content (OCR + NLP)
✓ Confirm that the file is readable
✓ Prevent garbage/unrelated files
✓ Provide a basic authenticity score (demo-level)
✓ Detect if the document looks edited or suspicious (simple heuristics)

Example of AI outputs messages:
	•	"ai_verdict": "No suspicious metadata"
	•	“File quality good. No corruption found.”
	•	“Hash ready for blockchain storage.”

This makes the verification look intelligent, not just hashing.

⸻

Next step, execution of DocumentVerifier.sol:

 1. Open the Contract in Remix
	1.	Go to https://remix.ethereum.org
	2.	In the left sidebar, click File Explorer
	3.	Click Upload File
	4.	Upload DocumentVerifier.sol

Now the contract will appear in the left file panel.

 2. Compile the Smart Contract
	1.	Click the Solidity Compiler icon (looks like “S”).
	2.	Select compiler version 0.8.x (same as in the contract).
	3.	Click ▶ Compile DocumentVerifier.sol

If it turns green → compilation successful.

3. Deploy the Contract
	1.	Click the Deploy & Run Transactions icon (Ethereum logo).
	2.	Make sure the contract selected is DocumentVerifier.
   3.	Click Deploy.

A deployed contract instance will appear at the bottom. List down it.

4. Register the Hash

Your Python script (run_demo.py) had given you a hash in previous step like:  "0xa4b73c9f…something"

Now, list down the deployed contract;
- Under REGISTERDOCUMENT section, paste the hash and register it.
- Next, under "registered" section repaste the hash to check whether the hash is registered or not. (answer will come in form of boolean)
- Last but not the least, Verify the Document
       to check whether the document exists on blockchain:
      	1.	Paste the same hash.
      	2.	Click call.

       You will receive:
	      •	true → document is registered (original)
	      •	false → document is NOT registered (not original)

⸻

 Conclusion

The AI-Powered Blockchain Document Verifier is a demo prototype that shows how AI and blockchain can work together to verify the authenticity of digital documents.
Using Python, the system generates a document hash and performs a basic AI-based originality check.
Using Solidity, the hash is registered and verified on the blockchain to ensure tamper-proof validation.

Although this project is simple, it demonstrates a big concept:
AI can analyze documents, and blockchain can guarantee their integrity.

With more advanced features—like deepfake detection, NLP-based fraud analysis, and automated on-chain verification—this prototype could evolve into a fully reliable document authentication system for universities, companies, and government platforms.

This demo is only a first step, but it proves the potential of combining AI + Blockchain for secure and transparent document verification in the future.









