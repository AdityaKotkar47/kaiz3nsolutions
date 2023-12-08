import requests

def get_user_input():
    question = input("Enter the question: ")
    input_format = input("Enter the input format: ")
    output_format = input("Enter the output format: ")
    
    # Allow blank input for source
    source = input("Enter the source (press Enter if none): ").strip()
    if not source:
        source = "No source provided"

    # Prompt the user to enter the file path containing the C code
    code_file_path = input("Enter the file path containing the C code: ")
    with open(code_file_path, 'r') as code_file:
        code = code_file.read()

    return question, input_format, output_format, source, code

def generate_html_code(question, input_format, output_format, source, code):
    # Format the inputs into the HTML code
    html_code = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <title>Code Snippet with Copy Button</title>
    <link rel="stylesheet" href="https://cdn.rawgit.com/google/code-prettify/master/src/prettify.css">
    <style>
        /* Add your styling if needed */
        pre {{
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow: auto;
        }}
        button {{
            margin-top: 10px;
            padding: 8px 15px;
            font-size: 14px;
            background-color: #3498db;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }}
        button:hover {{
            background-color: #2980b9;
        }}
    </style>
</head>
<body>

<!-- Question -->
<h2>Question:</h2>
<p>{question}</p>

<!-- Code Snippet with Prettify -->
<h3>Code Snippet:</h3>
<pre class="prettyprint" id="codeSnippet">
<code class="language-c">
{code}
</code>
</pre>

<!-- Copy Button -->
<button onclick="copyCode()">Copy Code</button>

<!-- Include Prettify JS -->
<script src="https://cdn.rawgit.com/google/code-prettify/master/src/prettify.js"></script>
<script>
    function copyCode() {{
        const codeSnippet = document.getElementById('codeSnippet');
        const range = document.createRange();
        range.selectNode(codeSnippet);
        window.getSelection().removeAllRanges();
        window.getSelection().addRange(range);
        document.execCommand('copy');
        window.getSelection().removeAllRanges();
        alert('Code copied to clipboard!');
    }}
    // Run Prettify
    PR.prettyPrint();
</script>

</body>
</html>
"""

    # Print the generated HTML code
    print(html_code)


def main():
    question, input_format, output_format, source, code = get_user_input()
    generate_html_code(question, input_format, output_format, source, code)

if __name__ == "__main__":
    main()
