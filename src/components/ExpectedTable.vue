<template>
    <table id="expected-table" class="table table-striped table-responsive">
        <thead>
            <th class="col-xs-1 col-sm-1 line-no" v-on:click="sort('id')">#</th>
            <th class="col-xs-3 col-sm-2 expection" v-on:click="sort('score')">期待値</th>
            <th class="col-xs-9 col-sm-9" v-on:click="sort('max_value')">候補</th>
        </thead>
        <tbody>
          <tr v-for="x in expectedLines"
              v-bind:class="{ 'expected-1': classObject['expected-1_' + x.id], 'expected-2': classObject['expected-2_' + x.id] }"
              v-on:click="$emit('selectLine', x.id)">

            <th class="line-no">{{ x.id }}</th>
            <td class="expection">{{ x.score.toFixed(2) }}</td>
            <td>{{ x.values }}</td>
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
      let scores = this.expectedLines.map(x => x.score)
        .filter((x, i, self) => self.indexOf(x) === i)
        .sort((a, b) => b - a)

      let ret = {}
      for (let x of this.expectedLines) {
        if (scores[0] == x.score) {
          this.$emit('selectLine', x.id)
          ret["expected-1_" + x.id] = true
        } else if (scores[1] == x.score) {
          ret["expected-2_" + x.id] = true
        }
      }
      return ret
    }
  },
  methods: {
    sort: function(mode) {
      if (mode === "id") {
        this.expectedLines.sort((a, b) => a.id - b.id)
      }
      else if (mode == "score") {
        this.expectedLines.sort((a, b) => b.score - a.score || b.values[0] - a.values[0])
      }
      else if (mode == "max_value") {
        this.expectedLines.sort((a, b) => b.values[0] - a.values[0] || b.score - a.score)
      }
    },
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
