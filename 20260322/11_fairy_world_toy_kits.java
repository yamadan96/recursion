// Productインターフェース（全部品が実装）
interface Product {
    int getCosts();
}

// 各部品クラス
class Head implements Product {
    String description;
    int difficulty;
    int cost;

    Head(String description, int difficulty, int cost) {
        this.description = description;
        this.difficulty = difficulty;
        this.cost = cost;
    }

    public int getCosts() { return cost; }
    public String toString() { return description; }
}

class Body implements Product {
    String description;
    int difficulty;
    int cost;
    String sound;

    Body(String description, int difficulty, int cost, String sound) {
        this.description = description;
        this.difficulty = difficulty;
        this.cost = cost;
        this.sound = sound;
    }

    public int getCosts() { return cost; }
    public String makeSound() { return sound != null ? sound : "..."; }
    public String toString() { return description; }
}

class LeftArm implements Product {
    String description;
    int difficulty;
    int cost;

    LeftArm(String description, int difficulty, int cost) {
        this.description = description;
        this.difficulty = difficulty;
        this.cost = cost;
    }

    public int getCosts() { return cost; }
    public String toString() { return description; }
}

class RightArm implements Product {
    String description;
    int difficulty;
    int cost;

    RightArm(String description, int difficulty, int cost) {
        this.description = description;
        this.difficulty = difficulty;
        this.cost = cost;
    }

    public int getCosts() { return cost; }
    public String toString() { return description; }
}

class Legs implements Product {
    String description;
    int difficulty;
    int cost;

    Legs(String description, int difficulty, int cost) {
        this.description = description;
        this.difficulty = difficulty;
        this.cost = cost;
    }

    public int getCosts() { return cost; }
    public String walk() { return "walking"; }
    public String toString() { return description; }
}

// 抽象ファクトリー
abstract class HumanoidToyKitFactory {
    abstract Head createHead();
    abstract Body createBody();
    abstract LeftArm createLeftArm();
    abstract RightArm createRightArm();
    abstract Legs createLegs();
}

// 具象ファクトリー1: サイバーヴァンパイア
class CyberVampireKitFactory extends HumanoidToyKitFactory {
    Head createHead() {
        return new Head("Glowing eyes head with fang switch", 3, 500);
    }
    Body createBody() {
        return new Body("Black cape body", 2, 800, "Bat sound");
    }
    LeftArm createLeftArm() {
        return new LeftArm("Clawed left arm", 2, 300);
    }
    RightArm createRightArm() {
        return new RightArm("Right arm holding blood cup", 3, 400);
    }
    Legs createLegs() {
        return new Legs("Cold ruthless legs", 1, 300);
    }
}

// 具象ファクトリー2: ロボット
class RobotKitFactory extends HumanoidToyKitFactory {
    Head createHead() {
        return new Head("LED antenna head", 4, 600);
    }
    Body createBody() {
        return new Body("Metal armor body", 3, 900, "Beep");
    }
    LeftArm createLeftArm() {
        return new LeftArm("Drill left arm", 4, 500);
    }
    RightArm createRightArm() {
        return new RightArm("Laser gun right arm", 4, 500);
    }
    Legs createLegs() {
        return new Legs("Caterpillar legs", 3, 400);
    }
}

// 具象ファクトリー3: ウェアウルフ
class WerewolfKitFactory extends HumanoidToyKitFactory {
    Head createHead() {
        return new Head("Sharp fanged wolf head", 2, 400);
    }
    Body createBody() {
        return new Body("Fur covered body", 2, 700, "Howl");
    }
    LeftArm createLeftArm() {
        return new LeftArm("Hooked claw left arm", 2, 300);
    }
    RightArm createRightArm() {
        return new RightArm("Hooked claw right arm", 2, 300);
    }
    Legs createLegs() {
        return new Legs("Muscular legs", 1, 250);
    }
}

// おもちゃ組み立て関数
class Main {
    public static Product[] createAHumanoidToyByKit(HumanoidToyKitFactory factory) {
        Head head = factory.createHead();
        Body body = factory.createBody();
        LeftArm leftArm = factory.createLeftArm();
        RightArm rightArm = factory.createRightArm();
        Legs legs = factory.createLegs();

        Product[] parts = {head, body, leftArm, rightArm, legs};
        int totalCost = 0;
        int maxDifficulty = 0;
        for (Product p : parts) totalCost += p.getCosts();
        maxDifficulty = Math.max(head.difficulty, Math.max(body.difficulty,
            Math.max(leftArm.difficulty, Math.max(rightArm.difficulty, legs.difficulty))));

        System.out.println("=== Toy Complete! ===");
        System.out.println("Head: " + head);
        System.out.println("Body: " + body);
        System.out.println("Left Arm: " + leftArm);
        System.out.println("Right Arm: " + rightArm);
        System.out.println("Legs: " + legs);
        System.out.println("Sound: " + body.makeSound());
        System.out.println("Action: " + legs.walk());
        System.out.println("Difficulty: " + maxDifficulty + "/5");
        System.out.println("Total Cost: " + totalCost);
        System.out.println();

        return parts;
    }

    public static void main(String[] args) {
        System.out.println("【Cyber Vampire Kit】");
        createAHumanoidToyByKit(new CyberVampireKitFactory());

        System.out.println("【Robot Kit】");
        createAHumanoidToyByKit(new RobotKitFactory());

        System.out.println("【Werewolf Kit】");
        createAHumanoidToyByKit(new WerewolfKitFactory());
    }
}
