<template>
  <div class="container" v-if="this.$session.exists()">
    <hr>
    <h3>Account details</h3>
    <div class="form-group">
      <label for="name">Name:</label>
      <input type="text" class="form-control" id="name" placeholder="Enter your name" name="name">
    </div>

    <div class="form-group">
      <label for="surname">Surname:</label>
      <input type="text" class="form-control" id="surname" placeholder="Enter your name" name="name">
    </div>

    <h3>Gender</h3>
    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio" name="genderOptions" id="male" value="Male" checked>
      <label class="form-check-label" for="male">Male</label>
    </div>

    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio" name="genderOptions" id="female" value="Female">
      <label class="form-check-label" for="female">Female</label>
    </div>

    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio" name="genderOptions" id="other" value="Male">
      <label class="form-check-label" for="other">Other</label>
    </div>

    <div class="form-group">
      <label for="weight">Weight:</label>
      <input type="number" class="form-control" id="weight" placeholder="50" name="weight">
    </div>

    <div class="form-group">
      <label for="height">Height:</label>
      <input type="number" class="form-control" id="height" placeholder="170" name="height">
    </div>

    <div class="form-group">
      <label for="hair_colour">Hair Colour:</label>
      <input type="text" class="form-control" id="hair_colour" placeholder="Enter your hair colour" name="hair_colour">
    </div>

    <div class="form-group">
      <label for="eye_colour">Eye Colour:</label>
      <input type="text" class="form-control" id="eye_colour" placeholder="Enter your eye colour" name="eye_colour">
    </div>

    <h3>Sexual Orientation</h3>
    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio" name="sexualOptions" id="hetero" value="Heterosexual" checked>
      <label class="form-check-label" for="hetero">Heterosexual</label>
    </div>

    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio" name="sexualOptions" id="homo" value="Homosexual">
      <label class="form-check-label" for="homo">Homosexual</label>
    </div>

    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio" name="sexualOptions" id="bi" value="Bisexual">
      <label class="form-check-label" for="bi">Bisexual</label>
    </div>

    <h3>Education:</h3>
    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio" name="eduOptions" id="uni" value="University" checked>
      <label class="form-check-label" for="uni">University</label>
    </div>

    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio" name="eduOptions" id="high" value="High School">
      <label class="form-check-label" for="high">High School</label>
    </div>

    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio" name="eduOptions" id="jun" value="Junior High School">
      <label class="form-check-label" for="jun">Junior High School</label>
    </div>

    <div>
      <label><input type="checkbox" value="">Smoke?</label><br>
      <label><input type="checkbox" value="">Drink?</label><br>
      <label><input type="checkbox" value="">Children?</label>
    </div>

    <div class="form-group">
      <label for="name">Status:</label>
      <input type="text" class="form-control" id="status" placeholder="Enter your status ex Student" name="status">
    </div>

    <div class="form-group">
      <label for="bio">Bio:</label>
      <textarea class="form-control" rows="5" placeholder="Talk about you" id="bio"></textarea>
    </div>

    <div class="form-group">
      <label for="pfp">Photo Profile:</label>
      <input type="file" name="pfp" class="form-control-file" id="pfp" @change="onFileChange">
    </div>

    <button class="btn btn-lg btn-danger">Update Info</button>
  </div>
</template>

<script>
export default {
  name: "Account",
  data() {
    return {
      pfp: null
    }
  },

  beforeCreate() {
    if (!this.$session.exists())
      this.$router.push('/login')
  },

  methods: {
    onFileChange(evt) {
      this.pfp = evt.target.files[0]
    }
  }
}
</script>