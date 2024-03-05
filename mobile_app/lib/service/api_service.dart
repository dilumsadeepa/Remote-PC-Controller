import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static Future<String> apiCall(String ipAddress, String command) async {
    final url = Uri.parse(
        'http://$ipAddress:12345/$command'); // Replace with your actual API endpoint
    try {
      final response = await http.get(url);
      if (response.statusCode == 200) {
        // Assuming the response is a JSON string, you can parse it
        final jsonResponse = json.decode(response.body);
        return jsonResponse[
            'message']; // Change 'message' to the actual key in your JSON response
      } else {
        throw Exception(
            'Failed to lock screen. Status code: ${response.statusCode}');
      }
    } catch (e) {
      throw Exception('Failed to lock screen. Error: $e');
    }
  }

  //copy

  static Future<String> apiCopy(
      String ipAddress, String command, String data) async {
    final url = Uri.parse('http://$ipAddress:12345/$command');

    try {
      final response = await http.post(
        url,
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({'data': data}),
      );

      if (response.statusCode == 200) {
        final jsonResponse = json.decode(response.body);
        return jsonResponse['response'];
      } else {
        throw Exception(
            'Failed to send data. Status code: ${response.statusCode}');
      }
    } catch (e) {
      throw Exception('Failed to send data. Error: $e');
    }
  }

  //past

  static Future<String> apiPaste(String ipAddress, String command) async {
    final url = Uri.parse('http://$ipAddress:12345/$command');

    try {
      final response = await http.get(url);

      if (response.statusCode == 200) {
        final jsonResponse = json.decode(response.body);
        return jsonResponse['response'];
      } else {
        throw Exception(
            'Failed to get clipboard data. Status code: ${response.statusCode}');
      }
    } catch (e) {
      throw Exception('Failed to get clipboard data. Error: $e');
    }
  }

  // Add other API calls for different commands as needed
}
