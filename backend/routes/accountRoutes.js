import express from 'express';
import {
    addMoneyToAccount,
    createAccount,
    getAccounts,
} from "../controllers/accountController.js";
import authMiddleware from "../middlewares/authMiddleware.js";

const router = express.Router();

router.get("/:id?", authMiddleware, getAccounts)
router.post("/create", authMiddleware, createAccount);
router.put("/add-money", authMiddleware, addMoneyToAccount);

export default router;