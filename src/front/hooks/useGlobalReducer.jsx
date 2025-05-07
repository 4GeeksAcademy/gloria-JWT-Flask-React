// src/front/hooks/useGlobalReducer.jsx

import { useContext, useReducer, createContext } from "react";
import storeReducer, { initialStore } from "../store";

// Crear el contexto para el estado global
const StoreContext = createContext();

// Componente Provider que provee el store y dispatch a toda la app
export function StoreProvider({ children }) {
    const [store, dispatch] = useReducer(storeReducer, initialStore());
    return (
        <StoreContext.Provider value={{ store, dispatch }}>
            {children}
        </StoreContext.Provider>
    );
}

// Hook personalizado para acceder al contexto
export default function useGlobalReducer() {
    const context = useContext(StoreContext);
    if (!context) {
        throw new Error("useGlobalReducer must be used within a StoreProvider");
    }
    return context;
}
