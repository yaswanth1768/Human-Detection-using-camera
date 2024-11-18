constexpr int motor_1_control_v{12};
constexpr int motor_2_control_v{14};

bool on{};

void setup()
{
  Serial.begin(9600);
  pinMode(motor_1_control_v, OUTPUT);
  pinMode(motor_2_control_v, OUTPUT);
}

void loop()
{
  while(Serial.available()) {
    char c = Serial.read();
    if(c == 49) {
      on = true;
    } 
    else if(c == 48) {
      on = false;
    }
    // Serial.println(Serial.read());
  }
  if(on) {
    digitalWrite(motor_1_control_v, HIGH);
    digitalWrite(motor_2_control_v, LOW);
  } else {q
    digitalWrite(motor_1_control_v, LOW);
    digitalWrite(motor_2_control_v, LOW);
  }

}