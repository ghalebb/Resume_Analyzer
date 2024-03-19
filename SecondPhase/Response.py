class Response:
    def __init__(self, result_json, spelling_errors):
        """
        Initialize the Response object with results from checks and spelling errors.

        :param result_json: JSON object containing the results of various checks
        :param spelling_errors: List of strings representing spelling errors
        """
        self.result_json = result_json
        self.spelling_errors = spelling_errors

    def generate_response(self):
        """
        Generate a comprehensive response based on the check results and spelling errors.

        :return: A formatted string containing the response to be given to the user.
        """
        responses = []

        for check, result in self.result_json.items():
            if result.lower() == "no":
                response = f"✅ {check.replace('_', ' ')} check passed."
            else:
                response = f"❌ {check.replace('_', ' ')} check failed: {result}."
            responses.append(response)

        if self.spelling_errors:
            spelling_response = "Found spelling errors: " + ", ".join(self.spelling_errors)
            responses.append(spelling_response)
        else:
            responses.append("✅ No spelling errors found.")
        final_response = "\n".join(responses)
        return final_response


# if __name__ == '__main__':
#     result_json = {
#         "ResidenceLocationCheck": "No",
#         # Add other checks here
#     }
#     spelling_errors = ["wrod1", "wrod2"]
#
#     response_generator = Response(result_json, spelling_errors)
#     user_response = response_generator.generate_response()
#     print(user_response)
