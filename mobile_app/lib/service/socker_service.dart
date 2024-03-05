import 'dart:io';

void sendCommand() async {
  final socket = await Socket.connect('192.168.8.119', 12345);

  // Send a command to the server
  socket.write('lock');

  // Listen for responses from the server
  socket.listen(
    (List<int> data) {
      final response = String.fromCharCodes(data);
      print('Received response from server: $response');
    },
    onDone: () {
      print('Connection closed by the server.');
      socket.destroy();
    },
    onError: (error) {
      print('Error: $error');
      socket.destroy();
    },
    cancelOnError: true,
  );
}
