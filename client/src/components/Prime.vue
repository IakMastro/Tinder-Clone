<template>
  <div class="container">
    <h3>Plan</h3>
    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio" name="planOptions" id="one_month" value="12" checked>
      <label class="form-check-label" for="one_month">One Month - 12&euro;</label>
    </div>

    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio" name="planOptions" id="six_month" value="6">
      <label class="form-check-label" for="six_month">6 Month - 6&euro;</label>
    </div>

    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio" name="planOptions" id="twelve_month" value="5">
      <label class="form-check-label" for="twelve_month">One Month - 5&euro;</label>
    </div>

    <br>
    <button class="btn btn-lg btn-danger">Buy Prime</button>
  </div>
</template>

<script>
export default {
  name: "Prime"
}
</script>

<style scoped>

</style>