// fontawesome.js

import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

// Agrega los íconos que deseas utilizar
library.add(fas)

// Exporta solo el componente FontAwesomeIcon
export { FontAwesomeIcon }
