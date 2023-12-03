from flask import Flask, request, jsonify
from utils import parse_gym_notes

app = Flask(__name__)

@app.route("/ping", methods=["GET", "POST"])
def ping():
    return jsonify({"Ping": "GymNotes pong!!"}), 200

@app.route("/parse", methods=["POST"])
def parse():
    user = request.args.get("user", "")
    notes = request.json.get("notes", "")
    print(f"Input: {notes}")
    try:
        output = parse_gym_notes(notes)
        header = "DateTime, Muscle Group, Exercise Name, Sets, Reps, Weight\n"
        try:
            lines = open("/outputs/{}.csv".format(user)).readlines()[1:]
            lines = header + lines + output
        except Exception:
            lines = header + output
        with open("/outputs/{}.csv".format(user), "w") as fi:
            for l in lines:
                fi.write(l)
        return jsonify({"message": output})
    except Exception as e:
        print(e)
        return jsonify({"message": f"{e}"}), 404

if __name__ == "__main__":  
    app.run()