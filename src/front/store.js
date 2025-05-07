export const initialStore = () => ({
  token: null,
});

export default function storeReducer(store, action = {}) {
  switch (action.type) {
      case "updateToken":
          return {
              ...store,
              token: action.payload,
          };
      default:
          return store;
  }
}