// ignore_for_file: prefer_const_constructors_in_immutables, library_private_types_in_public_api, prefer_const_constructors, use_build_context_synchronously

import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:remote_pc/pages/commandview.dart';

class Home extends StatefulWidget {
  Home({super.key});

  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  TextEditingController ipAddress = TextEditingController();

  Future<bool> checkConnection(String ipAddress) async {
    try {
      final response = await http.get(Uri.parse('http://$ipAddress:12345/check'));
      if (response.statusCode == 200) {
        final jsonResponse = json.decode(response.body);
        return jsonResponse['message'] == 'yes';
      } else {
        return false;
      }
    } catch (e) {
      return false;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        toolbarHeight: 10,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              "Welcome to Remote PC\n Controller",
              style: TextStyle(
                fontSize: 20,
                fontWeight: FontWeight.bold,
                color: Colors.blue[400],
              ),
              textAlign: TextAlign.center,
            ),
            Icon(
              Icons.computer,
              size: 150,
              color: Colors.greenAccent[400],
            ),
            Padding(
              padding: const EdgeInsets.all(30),
              child: TextField(
                controller: ipAddress,
                decoration: InputDecoration(
                  labelText: "Enter the IP Address that shown on PC",
                ),
                keyboardType: TextInputType.number,
              ),
            ),
            ElevatedButton(
              onPressed: () async {
                String enteredIPAddress = ipAddress.text;

                // Check the connection before navigating to Commandview
                bool isConnectionOk = await checkConnection(enteredIPAddress);

                if (isConnectionOk) {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => Commandview(ipAddress: enteredIPAddress),
                    ),
                  );
                } else {
                  // Show a suggestion to check the PC and mobile in the same network
                  ScaffoldMessenger.of(context).showSnackBar(
                    SnackBar(
                      content: Text('Connection error. Make sure both devices are on the same network and make sure pc software is turn on'),
                      duration: Duration(seconds: 10),
                    ),
                  );
                }
              },
              style: ButtonStyle(
                backgroundColor: MaterialStateProperty.all<Color>(Colors.blue),
                minimumSize: MaterialStateProperty.all<Size>(Size(200, 60)),
              ),
              child: Text("Start", style: TextStyle(fontSize: 18, color: Colors.white)),
            ),
          ],
        ),
      ),
    );
  }
}
