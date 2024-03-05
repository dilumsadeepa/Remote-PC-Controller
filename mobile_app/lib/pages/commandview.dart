// ignore_for_file: prefer_const_constructors, use_build_context_synchronously

import 'package:flutter/material.dart';
import 'package:remote_pc/service/api_service.dart';
import 'package:confirm_dialog/confirm_dialog.dart';
import 'package:flutter/services.dart';

class Commandview extends StatelessWidget {
  final String ipAddress;

  const Commandview({super.key, required this.ipAddress});

  void _sendCopy(BuildContext context, String command) async {
    String copydata = "";
    try {
      // Get current clipboard data
      ClipboardData? clipboardData =
          await Clipboard.getData(Clipboard.kTextPlain);
      if (clipboardData != null && clipboardData.text != null) {
        copydata = clipboardData.text!;
      }

      if (await confirm(context)) {
        String response =
            await ApiService.apiCopy(ipAddress, command, copydata);
        // Show response as a toast message
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text(response),
            duration: Duration(seconds: 2),
          ),
        );
      }
    } catch (e) {
      // Handle error, for example, show an error toast message
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text('Error: $e'),
          duration: Duration(seconds: 15),
        ),
      );
    }
  }

  void _sendPaste(BuildContext context, String command) async {
    try {
      if (await confirm(context)) {
        String response = await ApiService.apiPaste(ipAddress, command);

        await Clipboard.setData(ClipboardData(text: response));

        // Show response as a toast message
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text("Successfully Copied"),
            duration: Duration(seconds: 2),
          ),
        );
      }
    } catch (e) {
      // Handle error, for example, show an error toast message
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text('Error: $e'),
          duration: Duration(seconds: 15),
        ),
      );
    }
  }

  void _sendData(BuildContext context, String command) async {
    try {
      if (await confirm(context)) {
        String response = await ApiService.apiCall(ipAddress, command);
        // Show response as a toast message
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text(response),
            duration: Duration(seconds: 2),
          ),
        );
      }
    } catch (e) {
      // Handle error, for example, show an error toast message
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text('Error: $e'),
          duration: Duration(seconds: 15),
        ),
      );
    }
  }

  void _sendDataWac(BuildContext context, String command) async {
    try {
      String response = await ApiService.apiCall(ipAddress, command);
      // Show response as a toast message
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(response),
          duration: Duration(seconds: 2),
        ),
      );
    } catch (e) {
      // Handle error, for example, show an error toast message
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text('Error: $e'),
          duration: Duration(seconds: 15),
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Command View"),
      ),
      body: GridView.count(
        crossAxisCount: 3,
        crossAxisSpacing: 16.0,
        mainAxisSpacing: 16.0,
        padding: EdgeInsets.all(16.0),
        children: [
          buildCommandIconButton(
              Icons.lock, 'Lock', () => _sendData(context, "lock")),
          buildCommandIconButton(Icons.desktop_windows, 'Max or Min',
              () => _sendData(context, "minmax")),
          buildCommandIconButton(
              Icons.close, 'Close window', () => _sendData(context, "close")),
          buildCommandIconButton(
              Icons.bedtime, 'Sleep', () => _sendData(context, "sleep")),
          buildCommandIconButton(Icons.power_settings_new, 'Shutdown',
              () => _sendData(context, "poweroff")),
          buildCommandIconButton(Icons.restart_alt, 'Restart',
              () => _sendData(context, "restart")),
          buildCommandIconButton(
              Icons.copy, 'Copy', () => _sendCopy(context, "copy")),
          buildCommandIconButton(
              Icons.paste, 'Paste', () => _sendPaste(context, "paste")),
          buildCommandIconButton(
              Icons.window, 'Win key', () => _sendDataWac(context, "winkey")),
          buildCommandIconButton(Icons.skip_previous, 'Previous',
              () => _sendDataWac(context, "prev")),
          buildCommandIconButton(
              Icons.arrow_upward, 'Up', () => _sendDataWac(context, "upa")),
          buildCommandIconButton(
              Icons.skip_next, 'Next', () => _sendDataWac(context, "next")),
          buildCommandIconButton(Icons.keyboard_arrow_left, 'Left',
              () => _sendDataWac(context, "lefta")),
          buildCommandIconButton(Icons.play_arrow, 'Play/Pause',
              () => _sendDataWac(context, "play")),
          buildCommandIconButton(Icons.keyboard_arrow_right, 'Right',
              () => _sendDataWac(context, "righta")),
          buildCommandIconButton(Icons.keyboard_tab, 'Tab Key',
              () => _sendDataWac(context, "tabk")),
          buildCommandIconButton(Icons.arrow_downward, 'Down',
              () => _sendDataWac(context, "downa")),
          buildCommandIconButton(Icons.keyboard_return, 'Enter',
              () => _sendDataWac(context, "enterk")),

          buildCommandIconButton(Icons.volume_down, 'Volume Down',
              () => _sendDataWac(context, "vd")),

          buildCommandIconButton(Icons.volume_mute, 'Volume Mute',
              () => _sendDataWac(context, "vm")),
            
          buildCommandIconButton(Icons.volume_up, 'Volume Up',
              () => _sendDataWac(context, "vu")),



        ],
      ),
    );
  }

  Widget buildCommandIconButton(
      IconData icon, String label, VoidCallback onPressed) {
    return InkWell(
      onTap: onPressed,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(icon, size: 36.0),
          SizedBox(height: 8.0),
          Text(label),
        ],
      ),
    );
  }
}
