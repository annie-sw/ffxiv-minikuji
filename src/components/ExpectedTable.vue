<template>
    <table id="expected-table" class="table table-striped table-responsive">
        <thead>
            <th class="col-xs-1 col-sm-1 line-no">#</th>
            <th class="col-xs-3 col-sm-2 expection">期待値</th>
            <th class="col-xs-9 col-sm-9">候補</th>
        </thead>
        <tbody>
          <tr v-for="(v, k) in expectedLines"
              v-bind:class="{ 'expected-1': classObject['expected-1_' + k], 'expected-2': classObject['expected-2_' + k] }"
              v-on:click="$emit('selectLine', k)">
            <th class="line-no">{{ k }}</th>
            <td class="expection">{{ v.score }}</td>
            <td>{{ v.values }}</td>
          </tr>
        </tbody>
    </table>
</template>

<script>
export default {
  name: "expected-table",
  props: ["expectedLines"],
  computed: {
    classObject: function() {
      // 重複排除した降順のスコアリストを作成
      let scores = Object.values(this.expectedLines)
        .map(x => x.score)
        .filter((x, i, self) => self.indexOf(x) === i)
        .sort((a, b) => b - a)

      let ret = {}
      for (let i in this.expectedLines) {
        let score = this.expectedLines[i].score
        if (scores[0] == score) {
          this.$emit('selectLine', i)
          ret["expected-1_" + i] = true
        } else if (scores[1] == score) {
          ret["expected-2_" + i] = true
        }
      }

      return ret
    }
  }
}
</script>

<style>
#expected-table .expected-1 {
    background-color: #ccffff;
}
#expected-table .expected-2 {
    /* background-color: #ccffcc; */
    background-color: #eeffff;
}
#expected-table .line-no {
    text-align: center;
}
#expected-table .expection {
    text-align: center;
}
#expected-table {
    margin-top: 10px;
}
</style>
